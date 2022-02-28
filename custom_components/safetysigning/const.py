"""Define constants used in garbage_collection."""

# Constants for crons.
# Base component constants
DOMAIN = "crons"
TOKEN_PLATFORM = "token"
ATTRIBUTION = "Data from this is provided by crons."

VERSION = 2

ATTR_NEXT_DATE = "next_date"
ATTR_NEXT_HOLIDAY = "next_cron"
ATTR_LAST_UPDATED = "last_updated"
ATTR_HOLIDAYS = "crons"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"
DEVICE_CLASS = "crons__schedule"

# Configuration
CONF_TOKEN = "token"
CONF_ICON_NORMAL = "icon_normal"
CONF_ICON_TODAY = "icon_today"
CONF_ICON_TOMORROW = "icon_tomorrow"
CONF_COUNTRY = "country"
CONF_HOLIDAY_POP_NAMED = "cron_pop_named"
CONF_PROV = "prov"  # obsolete
CONF_STATE = "state"  # obsolete
CONF_SUBDIV = "subdiv"  # Subdivision - replaces state and prov
CONF_OBSERVED = "observed"
CONF_TOKENS = "tokens"

# Defaults
DEFAULT_NAME = DOMAIN

# Icons
DEFAULT_ICON_NORMAL = "mdi:cellphone-key"
DEFAULT_ICON_TODAY = "mdi:calendar-arrow-right"
DEFAULT_ICON_TOMORROW = "mdi:cellphone-check"
ICON = DEFAULT_ICON_NORMAL
