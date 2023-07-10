provider "docker" {
     host = "unix:///var/run/docker.sock"
   }

   resource "docker_image" "ubuntu" {
     name = "ubuntu:latest"
   }

   resource "docker_container" "ubuntu" {
     image = "${docker_image.ubuntu.latest}"
     name  = "ubuntu"
   }

   resource "docker_image" "flask" {
     name = "flask:latest"
   }

   resource "docker_container" "flask" {
     image = "${docker_image.flask.latest}"
     name  = "flask"
     ports {
       internal = 5000
       external = 5000
     }
   }