from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.account.models import User
from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager


class Event(TimeStampedModel):
    class EventType(models.TextChoices):
        APPEARANCE_SIGNING = "Appearnace or Signing", _("Appearance or Signing")
        ATTRACTION = "Attraction", _("Attraction")
        CAMP_TRIP_RETREAT = "Camp, Trip or Retreat", _("Camp, Trip or Retreat")
        CLASS_TRAINING_WORKSHOP = "Class, Training or Workshop", _("Class, Training or Workshop")
        CONCERT_PERFORMANCE = "Concert or Performance", _("Concert or Performance")
        CONFERENCE = "Conference", _("Conference")
        CONVENTION = "Convention", _("Convention")
        DINNER_GALA = "Dinner or Gala", _("Dinner or Gala")
        FESTIVAL_FAIR = "Festival or Fair", _("Festival or Fair")
        GAME_COMPETITION = "Game or Competition", _("Game or Competition")
        MEETING_NETWORKING = "Meeting or Networking Event", _("Meeting or Networking Event")
        OTHER = "Other", _("Other")
        PARTY_SOCIAL_GATHERING = "Party or Social Gathering", _("Party or Social Gathering")
        RACE_ENDURANCE = "Race or Enduarance Event", _("Race or Endurance Event")
        RALLY = "Rally", _("Rally")
        SCREENING = "Screening", _("Screening")
        SEMINAR_TALK = "Seminar or Talk", _("Seminar or Talk")
        TOUR = "Tour", _("Tour")
        TOURNAMENT = "Tournament", _("Tournament")
        TRADE_SHOW = "Trade Show", _("Trade Show")

    class EventCategory(models.TextChoices):
        ART = "Art", _("Art")
        CULTURE = "Culture", _("Culture")
        EDUCATION = "Education", _("Education")
        ENTERTAINMENT = "Entertainment", _("Entertainment")
        FASHION = "Fashion", _("Fashion")
        FOOD = "Food", _("Food")
        HEALTH = "Health", _("Health")
        HISTORY = "History", _("History")
        HUMOR = "Humor", _("Humor")
        MUSIC = "Music", _("Music")
        NATURE = "Nature", _("Nature")
        OTHER = "Other", _("Other")
        SCIENCE = "Science", _("Science")
        SPORTS = "Sports", _("Sports")
        TECHNOLOGY = "Technology", _("Technology")
        TRAVEL = "Travel", _("Travel")

    class EventVenue(models.TextChoices):
        VENUE = "Venue", _("Venue")
        ONLINE = "Online Event", _("Online Event")
        TO_BE_ANNOUNCED = "To be Announced", _("To be Announced")

    title = models.CharField(_("Event Title"), max_length=255)
    sub_title = models.CharField(_("Event Sub-Title"), max_length=255, blank=True, null=True)
    description = models.TextField(_("Description"), blank=True)
    organizer = models.CharField(
        _("Organizer"), max_length=255, help_text=_("Tell Attendees who is organizing this event.")
    )
    type = models.CharField(_("Event Type"), max_length=255, choices=EventType.choices)
    category = models.CharField(_("Event Category"), max_length=255, choices=EventCategory.choices)
    background_image = models.ImageField(
        _("Background image"),
        upload_to="event/background_images/",
        blank=True,
        null=True,
    )
    tags = TaggableManager(
        _("Tags"),
        help_text=_("Improve discoverability of your event by adding tags relevant to the subject matter."),
        blank=True,
    )
    attendees = models.ManyToManyField(User, verbose_name=_("Users"), blank=True)
    location = models.CharField(_("Location"), max_length=100)
    start_time = models.DateTimeField(_("Start time"))
    end_time = models.DateTimeField(_("End time"))
    display_start_time = models.BooleanField(_("Display start time"), default=True)
    display_end_time = models.BooleanField(_("Display end time"), default=True)
    venue = models.CharField(_("Venue"), max_length=255, choices=EventVenue.choices)
    venue_location = models.CharField(_("Venue Location"), max_length=255, blank=True)

    def __str__(self):
        return self.title
