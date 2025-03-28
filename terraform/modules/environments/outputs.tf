# These could eventually be sourced from the phalanx repo
# This is a map output so that all of the enviroments can be iterated over
output "environments" {
  description = "Phalanx environments"
  value       = yamldecode(file("${path.module}/../../../data/environments.yaml"))
}
