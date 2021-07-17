from django.db import models
from sysapps.common import app_gv


class MasterDataRegistry(models.Model):
    app_name = models.CharField(max_length=255, db_index=True)
    app_display_name = models.CharField(max_length=255, blank=True, null=True)
    model_name = models.CharField(max_length=255, db_index=True)
    model_display_name = models.CharField(max_length=255, blank=True, null=True)
    displayable_fields = models.TextField(blank=True, null=True)
    form_fields = models.TextField(blank=True, null=True)
    sort_by_fields = models.TextField(blank=True, null=True)
    is_mc_required = models.BooleanField(default=False) # memcache: load table data in dynamic gv
    is_ui_required = models.BooleanField(default=False)
    created_on =  models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    datamode = models.CharField(max_length=1, default='A', choices=app_gv.DATAMODE_CHOICES)

    class Meta:
       verbose_name = 'MasterDataRegistry'
       verbose_name_plural = 'MasterDataRegistry'

    def __str__(self):
        return self.model_name


class KVMaster(models.Model):
    key_category = models.CharField(max_length=255, db_index=True)
    key_code = models.CharField(max_length=255, unique=True, db_index=True)
    key_name = models.CharField(max_length=255, db_index=True)
    key_value = models.CharField(max_length=255)
    key_desc = models.CharField(max_length=255, blank=True, null=True)
    data_loaded_by = models.CharField(max_length=10, default='USER', choices=app_gv.DATA_LOADED_BY_CHOICES) # Data loaded by System or entered by User
    created_on =  models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    datamode = models.CharField(max_length=1, default='A', choices=app_gv.DATAMODE_CHOICES)

    def __str__(self):
        return self.key_code

    class Meta:
        verbose_name = 'KVMaster'
        verbose_name_plural = 'KVMaster'


class Continent(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    datamode = models.CharField(max_length=1, default='A', choices=app_gv.DATAMODE_CHOICES)

    class Meta:
        verbose_name = 'Continent'
        verbose_name_plural = 'Continents'

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(unique=True, max_length=255)
    iso_4217_alpha = models.CharField(max_length=255)
    iso_4217_numeric = models.CharField(max_length=255)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    capital_city = models.CharField(max_length=255)
    telephone_calling_code = models.CharField(max_length=5)
    internet_domain_code = models.CharField(max_length=5)
    continent = models.ForeignKey(Continent,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    datamode = models.CharField(max_length=1, default='A', choices=app_gv.DATAMODE_CHOICES)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class CRegion(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    datamode = models.CharField(max_length=1, default='A', choices=app_gv.DATAMODE_CHOICES)

    class Meta:
        verbose_name = 'CRegion'
        verbose_name_plural = 'CRegions'

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    datamode = models.CharField(max_length=1, default='A', choices=app_gv.DATAMODE_CHOICES)

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, related_name='state_cities', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    datamode = models.CharField(max_length=1, default='A', choices=app_gv.DATAMODE_CHOICES)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Postalcode(models.Model):
    postalcode = models.CharField(unique=True, max_length=255)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    datamode = models.CharField(max_length=1, default='A', choices=app_gv.DATAMODE_CHOICES)

    class Meta:
        verbose_name = 'PostalCode'
        verbose_name_plural = 'PostalCodes'

    def __str__(self):
        return self.postalcode


class Currency(models.Model):
    name = models.CharField(unique=True, max_length=255)
    currency_type = models.CharField(max_length=1, default='P', choices=app_gv.CURRENCY_TYPE_CHOICES)
    symbol = models.CharField(max_length=10, blank=True, null=True)
    iso_4217_alpha = models.CharField(max_length=10)
    iso_4217_numeric = models.IntegerField()
    major_unit_name = models.CharField(max_length=255, blank=True, null=True)
    minor_unit_name = models.CharField(max_length=255, blank=True, null=True)
    display_format = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    datamode = models.CharField(max_length=1, default='A', choices=app_gv.DATAMODE_CHOICES)

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return self.name


class TimeFormat(models.Model):
    name = models.CharField(unique=True, max_length=100)
    display_format = models.CharField(max_length=100)
    display_pattern = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    datamode = models.CharField(max_length=1, default='A', choices=app_gv.DATAMODE_CHOICES)

    class Meta:
        verbose_name = 'TimeFormat'
        verbose_name_plural = 'TimeFormats'

    def __str__(self):
        return self.name


class NameFormat(models.Model):
    name = models.CharField(unique=True, max_length=100)
    display_format = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    datamode = models.CharField(max_length=1, default='A', choices=app_gv.DATAMODE_CHOICES)

    class Meta:
        verbose_name = 'NameFormat'
        verbose_name_plural = 'NameFormats'

    def __str__(self):
        return self.name


class DateFormat(models.Model):
    name = models.CharField(unique=True, max_length=100)
    display_format = models.CharField(max_length=100)
    display_pattern = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    datamode = models.CharField(max_length=1, default='A', choices=app_gv.DATAMODE_CHOICES)

    class Meta:
        verbose_name = 'DateFormat'
        verbose_name_plural = 'DateFormats'

    def __str__(self):
        return self.name