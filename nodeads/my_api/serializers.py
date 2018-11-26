from rest_framework import serializers
from .models import Group, Element


class GroupSerializer(serializers.ModelSerializer):
    child_groups = serializers.SerializerMethodField('get_children_groups')
    child_elements = serializers.SerializerMethodField('get_children_elements')

    def get_children_groups(self, instance):
        query_groups = Group.objects.filter(parent_group_id=instance.id).values('id','name')
        return [entry for entry in query_groups] if query_groups else ''

    def get_children_elements(self, instance):
        query_groups = Element.objects.filter(parent_group_id=instance.id).filter(checked__isnull=False).values('id','name', 'checked')
        return [entry for entry in query_groups] if query_groups else ''


    class Meta:
        model = Group
        fields = ('id', 'parent_group_id', 'name', 'num_child_groups', 'num_child_elements', 'child_groups', 'child_elements')


class ElementSerializer(serializers.ModelSerializer):
    #parent_group = GroupSerializer(read_only=True)
    class Meta:
        model = Element
        fields = ('name', 'dscr', 'image', 'parent_group')
