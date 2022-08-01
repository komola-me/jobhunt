from rest_framework import serializers
from worker.models import Address
from worker.models import Experience, Education, WorkerProfile, LanguageLevel, ProfessionalArea


class LanguageLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageLevel
        fields = [
            'language', 'level',
        ]


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['region', 'district']
        depth = 1


class WorkingAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalArea
        fields = ['category', 'specialization']


class WorkerProfileSerializer(serializers.ModelSerializer):
    education_items = serializers.SerializerMethodField()
    language_items = serializers.SerializerMethodField()
    experience_items = serializers.SerializerMethodField()
    address_items = serializers.SerializerMethodField()
    workingarea_items = serializers.SerializerMethodField()

    class Meta:
        model = WorkerProfile
        fields = ['user', 'gender', 'dob', 'bio', 'image',
                  'phone', 'email', 'telegram', 'skills', 'education_items',
                  'language_items', 'experience_items', 'address_items', 'workingarea_items']

    def get_education_items(self, obj):
        worker_education_query = Education.objects.filter(
            worker=obj.id)
        serializer = EducationSerializer(worker_education_query, many=True)

        return serializer.data

    def get_language_items(self, obj):
        worker_language_query = LanguageLevel.objects.filter(
            worker=obj.id)
        serializer = LanguageLevelSerializer(worker_language_query, many=True)
        return serializer.data

    def get_experience_items(self, obj):
        worker_experience_query = Experience.objects.filter(
            worker=obj.id)
        serializer = ExperienceSerializer(worker_experience_query, many=True)
        return serializer.data

    def get_address_items(self, obj):
        worker_address_query = Address.objects.filter(
            user=obj.id)
        serializer = AddressSerializer(worker_address_query, many=True)
        return serializer.data

    def get_workingarea_items(self, obj):
        worker_workingarea_query = ProfessionalArea.objects.filter(
            user = obj.id
        )
        serializer = WorkingAreaSerializer(worker_workingarea_query, many=True)
        return serializer.data
