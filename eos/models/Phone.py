from __future__ import unicode_literals

from django.db import models
import json

class Phone(models.Model):

    imsi = models.CharField(max_length = 16, primary_key = True)
    operator = models.CharField(max_length = 20, blank = True)
    signal_q = models.PositiveSmallIntegerField(blank = True, null = True)
    reg_status = models.CharField(max_length = 32, blank = True)
    cipher_ind = models.NullBooleanField(blank = True, null = True)
    kc = models.CharField(max_length = 20, blank = True)
    kc_gprs = models.CharField(max_length = 20, blank = True)
    cipher_key = models.CharField(max_length = 32, blank = True)
    integrity_key = models.CharField(max_length = 32, blank = True)
    tmsi = models.CharField(max_length = 20, blank = True)
    tmsi_time = models.PositiveIntegerField(blank = True, null = True)
    lai = models.CharField(max_length = 12, blank = True)
    ptmsi = models.CharField(max_length = 8, blank = True)
    ptmsi_sign = models.CharField(max_length = 6, blank = True)
    rai = models.CharField(max_length = 10, blank = True)
    threshold = models.PositiveIntegerField(blank = True, null = True)
    phone_vendor = models.CharField(blank = True, max_length = 30)
    phone_model = models.CharField(blank = True, max_length = 10)
    firmware_version = models.CharField(blank = True, max_length =10)
    imei = models.CharField(blank = True, max_length = 17)

    def __str__(self):
        return self.imsi

    def get_self(self):
        #thats another comment test for branch
        return json.dumps({"imsi":self.imsi})

    def get_fields(self):
        #thats a comment from branch testing
        return [(field.name, field.value_to_string(self)) for field in Phone._meta.fields]