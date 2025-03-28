locals {
  frequency_conditions = var.renotify_interval != null ? [{ event_frequency = {
    comparison_type = "count"
    value           = 0
    interval        = var.renotify_interval
  } }] : []

  slack_workspace = "Rubin Observatory"
}
