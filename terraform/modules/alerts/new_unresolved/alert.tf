resource "sentry_issue_alert" "alert" {
  name         = "New and Unresolved - ${var.environment.name}"
  organization = var.organization.slug
  project      = var.project.slug
  environment  = var.environment.name
  frequency    = 5
  action_match = "any"

  conditions_v2 = [
    { first_seen_event = {} },
    { regression_event = {} },
  ]


  actions_v2 = [
    {
      slack_notify_service = {
        workspace = data.sentry_organization_integration.slack.id
        channel   = "#${var.environment.status_channel.name}"
      }
    }
  ]
}
