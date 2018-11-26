from tastypie.resources import ModelResource
from .models import Group, Element
from django.db import IntegrityError
from django.core.exceptions import SuspiciousOperation

class GroupResource(ModelResource):
    class Meta:
        queryset = Group.objects.all()
        fields = ['id', 'parent_group_id', 'name', 'num_child_groups', 'num_child_elements']
        allowed_methods = ['get']
        resource_name = 'group'

    def dehydrate(self, bundle):
        query_groups = Group.objects.filter(parent_group_id=bundle.data['id']).values('id','name')
        bundle.data['child_groups'] = [entry for entry in query_groups] if query_groups else ''

        query_elements = Element.objects.filter(checked__isnull=False).filter(parent_group_id=bundle.data['id']).values('id','name')
        bundle.data['child_elements'] = [entry for entry in query_elements] if query_elements else ''

        return bundle


class ElementResource(ModelResource):
    class Meta:
        queryset = Element.objects.all()
        resource_name = 'post_element'
        allowed_methods = ['post', 'put']

    def obj_create(self, bundle, request=None, **kwargs):
      name, dscr, image, parent_group_id = bundle.data['name'], bundle.data['dscr'], bundle.data['image'], bundle.data['parent_group_id']
      bundle.obj = Element(name=name, dscr=dscr, image=image, parent_group=Group.objects.filter(id=parent_group_id).first())
      bundle.obj.save()
      # try:
      #     bundle.obj = Element(name=name, dscr=dscr, image=image, parent_group_id=Group.objects.filter(id=parent_group_id).first())
      #     bundle.obj.save()
      # except IntegrityError:
      #     raise SuspiciousOperation('Error occured')
      # return bundle
