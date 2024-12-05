# Google provider configuration
provider "google" {
  project = var.project_id
  region  = var.region
}

# VPC Network
resource "google_compute_network" "default" {
  name = "default-network"
}

# Firewall rule for PostgreSQL (port 5432)
resource "google_compute_firewall" "allow_postgres" {
  name    = "allow-postgres"
  network = google_compute_network.default.self_link

  allow {
    protocol = "tcp"
    ports    = ["5432"]
  }

  source_ranges = ["0.0.0.0/0"] # Restrict this to specific IPs for better security
}

# Firewall rule for SSH (port 22)
resource "google_compute_firewall" "allow_ssh" {
  name    = "allow-ssh"
  network = google_compute_network.default.self_link

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }

  source_ranges = ["0.0.0.0/0"] # Restrict this to your IP range
  target_tags   = ["ssh"]
}

# Compute Engine instance for PostgreSQL
resource "google_compute_instance" "postgres_instance" {
  name         = "postgres-instance"
  machine_type = "e2-micro"
  zone         = var.zone

  tags = ["ssh"] # Ensures SSH firewall rule applies to this instance

  boot_disk {
    initialize_params {
      image = "projects/debian-cloud/global/images/family/debian-11"
      size  = 50 # Disk size in GB
    }
  }

  network_interface {
    network = google_compute_network.default.self_link

    access_config {
      # Enables external IP
    }
  }

  metadata_startup_script = <<-EOT
    #! /bin/bash
    apt-get update
    apt-get install -y postgresql
    systemctl enable postgresql
    systemctl start postgresql
  EOT
}

# Output the external IP address of the instance
output "postgres_external_ip" {
  value = google_compute_instance.postgres_instance.network_interface[0].access_config[0].nat_ip
  description = "External IP address of the PostgreSQL instance"
}

resource "google_cloud_run_service" "cloud_run_psql" {
  name     = "cloud-run-psql-app"
  location = var.region

  template {
    spec {
      containers {
        image = "gcr.io/${var.project_id}/cloud-run-psql-app" # Update with your container image
        env {
          name  = "POSTGRES_HOST"
          value = google_compute_instance.postgres_instance.network_interface[0].access_config[0].nat_ip
        }
        env {
          name  = "POSTGRES_PORT"
          value = "5432"
        }
        env {
          name  = "POSTGRES_USER"
          value = "postgres"
        }
        env {
          name  = "POSTGRES_PASSWORD"
          value = "your-secure-password"
        }
        env {
          name  = "POSTGRES_DB"
          value = "postgres" # Default database
        }
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}
