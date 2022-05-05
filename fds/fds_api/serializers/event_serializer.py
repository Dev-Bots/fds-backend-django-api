from rest_framework import serializers
from ..models import *
from django.shortcuts import get_object_or_404
from ..serializers import ClubSerializer , PlayerSerializer, ScoutSerializer



class EventSerializer(serializers.ModelSerializer):
    club = ClubSerializer()
    applicants = PlayerSerializer(many=True)
    candidates = PlayerSerializer(many=True)
    accepted_applicants = PlayerSerializer(many=True)
    scouts = ScoutSerializer(many=True)
    class Meta:
        model = Event
        fields = ['id', 'posted_date','starting_date', 'application_deadline','description', "required_positions", 'age_limit', 'education_level', 'location', 'gender', 'session_time_for_each', 'parameters', 'scouts', 'applicants', 'club', 'candidates', 'accepted_applicants']
        
        # depth= 1
    
    def get_fields(self):
        fields = super().get_fields()
        
        request = self.context.get("request", None)
        if request is not None:
            if request.method ==  'POST':
                fields.pop('applicants')
                fields.pop('candidates')
                fields.pop('accepted_applicants')
                fields.pop('club')
                fields.pop("parameters")


                
        return fields
       

    def create(self, validated_data):

        #getting club 
        club_id = self.context['request'].user.id
        club = get_object_or_404(Club, pk=club_id)

        scouts= validated_data["scouts"]
        validated_data.pop("scouts")

        #creating the event
        event = Event.objects.create(club=club, **validated_data)
        event.scouts.set(scouts)

        #getting or creating skills
        skill_phyicality = Skill.objects.get_or_create(club=club, name="Physicality", description="This quality shows the player's overall physical fitness like strength, balance etc..", weight_for_GK=3, weight_for_DEF=5, weight_for_MID=4, weight_for_STR=3, is_default=True)
        skill_pace = Skill.objects.get_or_create(club=club, name="Pace", description="This quality shows the player's movement ability like speed, acceleration and agiltiy.", weight_for_GK=1, weight_for_DEF=3, weight_for_MID=4, weight_for_STR=5, is_default=True)
        skill_shooting = Skill.objects.get_or_create(club=club, name="Shooting", description="This quality shows the player's ability to finish or score from distance.", weight_for_GK=1, weight_for_DEF=2, weight_for_MID=5, weight_for_STR=5, is_default=True)
        skill_dribbling = Skill.objects.get_or_create(club=club, name="Dribbling", description="This quality shows the player's ability travel with the ball and take on defenders 1v1.", weight_for_GK=1, weight_for_DEF=2, weight_for_MID=5, weight_for_STR=5, is_default=True)
        skill_defending = Skill.objects.get_or_create(club=club, name="Shooting", description="This quality shows the player's ability to defend, intercept and win the ball back to the team.", weight_for_GK=3, weight_for_DEF=5, weight_for_MID=4, weight_for_STR=2,is_default=True)
        skill_passing = Skill.objects.get_or_create(club=club, name="Passing", description="This quality shows the player's ability to accurately pass the ball and/or create scoring opportunities for a teammate.", weight_for_GK=2, weight_for_DEF=4, weight_for_MID=5, weight_for_STR=4, is_default=True)
        skill_mentality = Skill.objects.get_or_create(club=club, name="Mentality", description="This quality shows the player's drive to win, grit, and showing a good sportsmanship behaviour.", weight_for_GK=5, weight_for_DEF=5, weight_for_MID=5, weight_for_STR=5,is_default=True)
        skill_xFactor = Skill.objects.get_or_create(club=club, name="X-Factor", description="This quality shows a player's unique and special/additional talent.", weight_for_GK=5, weight_for_DEF=5, weight_for_MID=5, weight_for_STR=5, is_default=True)

        #attaching all of them to the event with parameters
        parameters = Parameters.objects.create(event = event)
        parameters.skills.add(skill_phyicality[0], skill_pace[0], skill_shooting[0], skill_dribbling[0], skill_defending[0], skill_passing[0], skill_mentality[0], skill_xFactor[0])

        return event
        
"""

    club = models.ForeignKey("club", on_delete=models.DO_NOTHING, related_name='events')
    starting_date = models.DateField(_("Event start date"), auto_now=False, auto_now_add=False, blank=False)
    application_deadline = models.DateField(_("Application Deadline"), auto_now=False, auto_now_add=False, blank=False)
    description = models.TextField(_("Description"))

    required_positions = models.CharField(_('Required positions'), max_length=50, choices=RequiredPossition.choices, blank=False) #multi options problem!!!!!

    age_limit = models.IntegerField(_("Age limit"), blank=False)
    education_level = models.CharField(_("Education level"), max_length=200)
    location = models.CharField(_("Education level"),blank=False, max_length=200)
    gender = models.CharField(_("Gender"), max_length=50, choices=Gender.choices, blank=False)
    session_time_for_each = models.IntegerField(_("Session time"), blank=False)
    
    applicants = models.ManyToManyField(Player, related_name='applicants', blank=True)
    candidates = models.ManyToManyField(Player, related_name='candidates', blank=True)
    accepted_applicants = models.ManyToManyField(Player, related_name='accepted_applicants', blank=True)

    scouts = models.ManyToManyField(Scout, related_name='assigned_eventd', blank=True)
    club = models.ForeignKey('club', on_delete=models.CASCADE)
    name = models.CharField(_('Skill name'), max_length=100, blank=False)
    description = models.TextField(_("Skill Description"), blank=False)weight_for_GK

    weight_for_GK = models.IntegerField(_("Level of importance for GKs"), choices=SkillWeight.choices, default=SkillWeight.MODERATE)
    weight_for_DEF = models.IntegerField(_("Level of importance for DEFs"), choices=SkillWeight.choices, default=SkillWeight.MODERATE)
    weight_for_MID = models.IntegerField(_("Level of importance for MIDs"), choices=SkillWeight.choices, default=SkillWeight.MODERATE)
    weight_for_STR = models.IntegerField(_("Level of importance for GK"), choices=SkillWeight.choices, default=SkillWeight.MODERATE)




"""