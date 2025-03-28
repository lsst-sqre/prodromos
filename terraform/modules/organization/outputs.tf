output "org" {
  description = "The Rubin Observatory Sentry Organization"
  value       = data.sentry_organization.org
}

output "teams" {
  description = "Teams in the Rubin Observatory Sentry Oranization"
  value = {
    square = data.sentry_team.square
  }
}
