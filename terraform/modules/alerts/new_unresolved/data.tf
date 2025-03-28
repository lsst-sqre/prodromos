data "sentry_organization_integration" "slack" {
  organization = var.organization.slug
  provider_key = "slack"
  name         = local.slack_workspace
}
