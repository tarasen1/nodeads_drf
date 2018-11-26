from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    dscr = models.CharField(max_length=128, blank=True, null=True)
    image = models.ImageField(blank=False, null=False)
    parent_group = models.ForeignKey('Group', null=True, blank=True, on_delete=models.CASCADE)

    @property
    def num_child_groups(self):
        return Group.objects.filter(parent_group=self).count()

    @property
    def num_child_elements(self):
        return Element.objects.filter(parent_group=self).filter(checked__isnull=False).count()

    def __str__(self):
        return 'id: {}, name: {}'.format(self.id, self.name)


class Element(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    dscr = models.CharField(max_length=128, blank=True, null=True)
    image = models.ImageField(blank=False, null=False)
    checked = models.BooleanField(default=None,null=True, blank=True)
    date_of_creation = models.DateField(auto_now_add=True)
    parent_group = models.ForeignKey('Group', on_delete=models.CASCADE)

    def __str__(self):
        return '{}, id: {}, name: {}'.format('Null' if self.checked is None else self.checked, self.id, self.name)
