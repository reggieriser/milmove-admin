from django.db import models


class Addresses(models.Model):
    id = models.UUIDField(primary_key=True)
    street_address_1 = models.CharField(max_length=255)
    street_address_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    street_address_3 = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses'


class BackupContacts(models.Model):
    id = models.UUIDField(primary_key=True)
    service_member_id = models.UUIDField()
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    permission = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'backup_contacts'


class BlackoutDates(models.Model):
    id = models.UUIDField(primary_key=True)
    transportation_service_provider = models.ForeignKey('TransportationServiceProviders', models.DO_NOTHING)
    start_blackout_date = models.DateTimeField()
    end_blackout_date = models.DateTimeField()
    traffic_distribution_list = models.ForeignKey('TrafficDistributionLists', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    source_gbloc = models.CharField(max_length=255, blank=True, null=True)
    market = models.CharField(max_length=255, blank=True, null=True)
    zip3 = models.IntegerField(blank=True, null=True)
    volume_move = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blackout_dates'


class ClientCerts(models.Model):
    id = models.UUIDField(primary_key=True)
    sha256_digest = models.CharField(max_length=64, blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    allow_dps_auth_api = models.BooleanField(blank=True, null=True)
    allow_orders_api = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client_certs'


class Documents(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    service_member = models.ForeignKey('ServiceMembers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'documents'


class DpsUsers(models.Model):
    id = models.UUIDField(primary_key=True)
    login_gov_email = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dps_users'


class DutyStations(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    affiliation = models.CharField(max_length=255)
    address = models.ForeignKey(Addresses, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    transportation_office = models.ForeignKey('TransportationOffices', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'duty_stations'


class FuelEiaDieselPrices(models.Model):
    id = models.UUIDField(primary_key=True)
    pub_date = models.DateField()
    rate_start_date = models.DateField()
    rate_end_date = models.DateField()
    eia_price_per_gallon_millicents = models.IntegerField()
    baseline_rate = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fuel_eia_diesel_prices'


class GblNumberTrackers(models.Model):
    sequence_number = models.IntegerField(blank=True, null=True)
    gbloc = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gbl_number_trackers'


class InvoiceNumberTrackers(models.Model):
    standard_carrier_alpha_code = models.TextField(primary_key=True)
    year = models.IntegerField()
    sequence_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invoice_number_trackers'
        unique_together = (('standard_carrier_alpha_code', 'year'),)


class Invoices(models.Model):
    id = models.UUIDField(primary_key=True)
    status = models.CharField(max_length=255)
    invoiced_date = models.DateTimeField()
    invoice_number = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    shipment = models.ForeignKey('Shipments', models.DO_NOTHING)
    approver = models.ForeignKey('OfficeUsers', models.DO_NOTHING)
    upload = models.ForeignKey('Uploads', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoices'


class MoveDocuments(models.Model):
    id = models.UUIDField(primary_key=True)
    move = models.ForeignKey('Moves', models.DO_NOTHING)
    document = models.ForeignKey(Documents, models.DO_NOTHING)
    move_document_type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    title = models.CharField(max_length=255)
    personally_procured_move = models.ForeignKey('PersonallyProcuredMoves', models.DO_NOTHING, blank=True, null=True)
    shipment = models.ForeignKey('Shipments', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'move_documents'
        unique_together = (('move', 'document'),)


MOVE_TYPES = [
    ('PPM', 'PPM'),
    ('HHG', 'HHG'),
    ('HHG_PPM', 'HHG with PPM'),
]

MOVE_STATUSES = [
    ['DRAFT', 'Draft'],
    ['SUBMITTED', 'Submited'],
    ['APPROVED', 'Approved'],
    ['COMPLETED', 'Completed'],
    ['CANCELED', 'Canceled'],
]


class Moves(models.Model):
    id = models.UUIDField(primary_key=True)
    selected_move_type = models.CharField(max_length=255, blank=True, null=True, choices=MOVE_TYPES)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    orders = models.ForeignKey('Orders', models.DO_NOTHING)
    status = models.CharField(max_length=255, choices=MOVE_STATUSES)
    locator = models.CharField(unique=True, max_length=6, blank=True, null=True)
    cancel_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moves'
        verbose_name = 'move'
        verbose_name_plural = 'moves'

    def __str__(self):
        return self.locator


class MovingExpenseDocuments(models.Model):
    id = models.UUIDField(primary_key=True)
    move_document = models.ForeignKey(MoveDocuments, models.DO_NOTHING)
    moving_expense_type = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    requested_amount_cents = models.IntegerField(blank=True, null=True)
    payment_method = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moving_expense_documents'


class OfficeEmails(models.Model):
    id = models.UUIDField(primary_key=True)
    transportation_office = models.ForeignKey('TransportationOffices', models.DO_NOTHING)
    email = models.TextField()
    label = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'office_emails'


class OfficePhoneLines(models.Model):
    id = models.UUIDField(primary_key=True)
    transportation_office = models.ForeignKey('TransportationOffices', models.DO_NOTHING)
    number = models.TextField()
    label = models.TextField(blank=True, null=True)
    is_dsn_number = models.BooleanField()
    type = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'office_phone_lines'


class OfficeUsers(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    last_name = models.TextField()
    first_name = models.TextField()
    middle_initials = models.TextField(blank=True, null=True)
    email = models.TextField(unique=True)
    telephone = models.TextField()
    transportation_office = models.ForeignKey('TransportationOffices', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'office_users'


class Orders(models.Model):
    id = models.UUIDField(primary_key=True)
    service_member = models.ForeignKey('ServiceMembers', models.DO_NOTHING)
    issue_date = models.DateField()
    report_by_date = models.DateField()
    orders_type = models.CharField(max_length=255)
    has_dependents = models.BooleanField()
    new_duty_station = models.ForeignKey(DutyStations, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uploaded_orders = models.ForeignKey(Documents, models.DO_NOTHING)
    orders_number = models.CharField(max_length=255, blank=True, null=True)
    orders_type_detail = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255)
    tac = models.CharField(max_length=255, blank=True, null=True)
    department_indicator = models.CharField(max_length=255, blank=True, null=True)
    spouse_has_pro_gear = models.BooleanField()
    orders_issuing_agency = models.TextField(blank=True, null=True)
    paragraph_number = models.TextField(blank=True, null=True)
    sac = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'

    def __str__(self):
        return '{}: {} to {}'.format(
            self.service_member.last_name,
            self.service_member.duty_station.name,
            self.new_duty_station.name)


class PersonallyProcuredMoves(models.Model):
    id = models.UUIDField(primary_key=True)
    move = models.ForeignKey(Moves, models.DO_NOTHING)
    size = models.CharField(max_length=255, blank=True, null=True)
    weight_estimate = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    planned_move_date = models.DateField(blank=True, null=True)
    pickup_postal_code = models.CharField(max_length=255, blank=True, null=True)
    additional_pickup_postal_code = models.CharField(max_length=255, blank=True, null=True)
    destination_postal_code = models.CharField(max_length=255, blank=True, null=True)
    days_in_storage = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255)
    has_additional_postal_code = models.BooleanField(blank=True, null=True)
    has_sit = models.BooleanField(blank=True, null=True)
    has_requested_advance = models.BooleanField()
    advance_id = models.UUIDField(blank=True, null=True)
    estimated_storage_reimbursement = models.CharField(max_length=255, blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    planned_sit_max = models.IntegerField(blank=True, null=True)
    sit_max = models.IntegerField(blank=True, null=True)
    incentive_estimate_min = models.IntegerField(blank=True, null=True)
    incentive_estimate_max = models.IntegerField(blank=True, null=True)
    advance_worksheet = models.ForeignKey(Documents, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personally_procured_moves'


class Reimbursements(models.Model):
    id = models.UUIDField(primary_key=True)
    requested_amount = models.IntegerField()
    method_of_receipt = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    requested_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reimbursements'


class SchemaMigration(models.Model):
    version = models.CharField(unique=True, max_length=14)

    class Meta:
        managed = False
        db_table = 'schema_migration'


class ServiceAgents(models.Model):
    id = models.UUIDField(primary_key=True)
    shipment = models.ForeignKey('Shipments', models.DO_NOTHING)
    role = models.TextField()
    email = models.TextField(blank=True, null=True)
    phone_number = models.TextField(blank=True, null=True)
    fax_number = models.TextField(blank=True, null=True)
    email_is_preferred = models.BooleanField(blank=True, null=True)
    phone_is_preferred = models.BooleanField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    company = models.TextField()

    class Meta:
        managed = False
        db_table = 'service_agents'


class ServiceMembers(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, unique=True)
    edipi = models.TextField(blank=True, null=True)
    affiliation = models.TextField(blank=True, null=True)
    rank = models.TextField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    middle_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    suffix = models.TextField(blank=True, null=True)
    telephone = models.TextField(blank=True, null=True)
    secondary_telephone = models.TextField(blank=True, null=True)
    personal_email = models.TextField(blank=True, null=True)
    phone_is_preferred = models.BooleanField(blank=True, null=True)
    text_message_is_preferred = models.BooleanField(blank=True, null=True)
    email_is_preferred = models.BooleanField(blank=True, null=True)
    residential_address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True, related_name='+')
    backup_mailing_address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True, related_name='+')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    social_security_number = models.ForeignKey('SocialSecurityNumbers', models.DO_NOTHING, blank=True, null=True)
    duty_station = models.ForeignKey(DutyStations, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_members'


class ShipmentLineItemDimensions(models.Model):
    id = models.UUIDField(primary_key=True)
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'shipment_line_item_dimensions'


class ShipmentLineItems(models.Model):
    id = models.UUIDField(primary_key=True)
    shipment = models.ForeignKey('Shipments', models.DO_NOTHING)
    tariff400ng_item = models.ForeignKey('Tariff400NgItems', models.DO_NOTHING)
    quantity_1 = models.IntegerField()
    quantity_2 = models.IntegerField()
    location = models.CharField(max_length=255)
    notes = models.TextField()
    status = models.CharField(max_length=255)
    submitted_date = models.DateTimeField()
    approved_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    invoice = models.ForeignKey(Invoices, models.DO_NOTHING, blank=True, null=True)
    amount_cents = models.IntegerField(blank=True, null=True)
    applied_rate = models.IntegerField(blank=True, null=True)
    item_dimensions = models.ForeignKey(ShipmentLineItemDimensions, models.DO_NOTHING, blank=True, null=True,
                                        related_name='+')
    crate_dimensions = models.ForeignKey(ShipmentLineItemDimensions, models.DO_NOTHING, blank=True, null=True,
                                         related_name='+')
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_line_items'


class ShipmentOffers(models.Model):
    id = models.UUIDField(primary_key=True)
    shipment = models.ForeignKey('Shipments', models.DO_NOTHING)
    transportation_service_provider = models.ForeignKey('TransportationServiceProviders', models.DO_NOTHING)
    administrative_shipment = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    accepted = models.BooleanField(blank=True, null=True)
    rejection_reason = models.CharField(max_length=255, blank=True, null=True)
    transportation_service_provider_performance = models.ForeignKey('TransportationServiceProviderPerformances',
                                                                    models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shipment_offers'


class Shipments(models.Model):
    id = models.UUIDField(primary_key=True)
    traffic_distribution_list = models.ForeignKey('TrafficDistributionLists', models.DO_NOTHING, blank=True, null=True)
    actual_pickup_date = models.DateTimeField(blank=True, null=True)
    actual_delivery_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    source_gbloc = models.CharField(max_length=255, blank=True, null=True)
    market = models.CharField(max_length=255, blank=True, null=True)
    book_date = models.DateField(blank=True, null=True)
    requested_pickup_date = models.DateField(blank=True, null=True)
    move = models.ForeignKey(Moves, models.DO_NOTHING)
    status = models.TextField()
    estimated_pack_days = models.IntegerField(blank=True, null=True)
    estimated_transit_days = models.IntegerField(blank=True, null=True)
    pickup_address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True,
                                       related_name='+')
    has_secondary_pickup_address = models.BooleanField()
    secondary_pickup_address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True,
                                                 related_name='+')
    has_delivery_address = models.BooleanField()
    delivery_address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True,
                                         related_name='+')
    has_partial_sit_delivery_address = models.BooleanField()
    partial_sit_delivery_address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True,
                                                     related_name='+')
    weight_estimate = models.IntegerField(blank=True, null=True)
    progear_weight_estimate = models.IntegerField(blank=True, null=True)
    spouse_progear_weight_estimate = models.IntegerField(blank=True, null=True)
    destination_gbloc = models.CharField(max_length=255, blank=True, null=True)
    service_member = models.ForeignKey(ServiceMembers, models.DO_NOTHING)
    pm_survey_planned_pack_date = models.DateTimeField(blank=True, null=True)
    pm_survey_planned_pickup_date = models.DateTimeField(blank=True, null=True)
    pm_survey_planned_delivery_date = models.DateTimeField(blank=True, null=True)
    pm_survey_weight_estimate = models.IntegerField(blank=True, null=True)
    pm_survey_progear_weight_estimate = models.IntegerField(blank=True, null=True)
    pm_survey_spouse_progear_weight_estimate = models.IntegerField(blank=True, null=True)
    pm_survey_notes = models.TextField(blank=True, null=True)
    pm_survey_method = models.TextField()
    net_weight = models.IntegerField(blank=True, null=True)
    gbl_number = models.CharField(max_length=255, blank=True, null=True)
    pm_survey_conducted_date = models.DateTimeField(blank=True, null=True)
    actual_pack_date = models.DateTimeField(blank=True, null=True)
    gross_weight = models.IntegerField(blank=True, null=True)
    tare_weight = models.IntegerField(blank=True, null=True)
    original_delivery_date = models.DateField(blank=True, null=True)
    original_pack_date = models.DateField(blank=True, null=True)
    pm_survey_completed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipments'


class SignedCertifications(models.Model):
    id = models.UUIDField(primary_key=True)
    submitting_user = models.ForeignKey('Users', models.DO_NOTHING)
    move = models.ForeignKey(Moves, models.DO_NOTHING)
    certification_text = models.TextField()
    signature = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'signed_certifications'


class SocialSecurityNumbers(models.Model):
    id = models.UUIDField(primary_key=True)
    encrypted_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_security_numbers'


class StorageInTransits(models.Model):
    id = models.UUIDField(primary_key=True)
    shipment = models.ForeignKey(Shipments, models.DO_NOTHING)
    sit_number = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    estimated_start_date = models.DateField()
    authorized_start_date = models.DateField(blank=True, null=True)
    actual_start_date = models.DateField(blank=True, null=True)
    out_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    authorization_notes = models.TextField(blank=True, null=True)
    warehouse_id = models.CharField(max_length=255)
    warehouse_name = models.TextField()
    warehouse_address = models.ForeignKey(Addresses, models.DO_NOTHING)
    warehouse_phone = models.TextField(blank=True, null=True)
    warehouse_email = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'storage_in_transits'


class Tariff400NgFullPackRates(models.Model):
    id = models.UUIDField(primary_key=True)
    schedule = models.IntegerField(blank=True, null=True)
    weight_lbs_lower = models.IntegerField(blank=True, null=True)
    weight_lbs_upper = models.IntegerField(blank=True, null=True)
    rate_cents = models.IntegerField(blank=True, null=True)
    effective_date_lower = models.DateField(blank=True, null=True)
    effective_date_upper = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tariff400ng_full_pack_rates'


class Tariff400NgFullUnpackRates(models.Model):
    id = models.UUIDField(primary_key=True)
    schedule = models.IntegerField(blank=True, null=True)
    rate_millicents = models.IntegerField(blank=True, null=True)
    effective_date_lower = models.DateField(blank=True, null=True)
    effective_date_upper = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tariff400ng_full_unpack_rates'


class Tariff400NgItemRates(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(max_length=255)
    schedule = models.IntegerField(blank=True, null=True)
    weight_lbs_lower = models.IntegerField()
    weight_lbs_upper = models.IntegerField()
    rate_cents = models.IntegerField()
    effective_date_lower = models.DateField()
    effective_date_upper = models.DateField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tariff400ng_item_rates'


class Tariff400NgItems(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(max_length=255)
    discount_type = models.CharField(max_length=255)
    allowed_location = models.CharField(max_length=255)
    item = models.CharField(max_length=255)
    measurement_unit_1 = models.CharField(max_length=255)
    measurement_unit_2 = models.CharField(max_length=255)
    rate_ref_code = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    requires_pre_approval = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tariff400ng_items'


class Tariff400NgLinehaulRates(models.Model):
    id = models.UUIDField(primary_key=True)
    distance_miles_lower = models.IntegerField(blank=True, null=True)
    distance_miles_upper = models.IntegerField(blank=True, null=True)
    weight_lbs_lower = models.IntegerField(blank=True, null=True)
    weight_lbs_upper = models.IntegerField(blank=True, null=True)
    rate_cents = models.IntegerField(blank=True, null=True)
    effective_date_lower = models.DateField(blank=True, null=True)
    effective_date_upper = models.DateField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tariff400ng_linehaul_rates'


class Tariff400NgServiceAreas(models.Model):
    id = models.UUIDField(primary_key=True)
    service_area = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    services_schedule = models.IntegerField(blank=True, null=True)
    linehaul_factor = models.IntegerField(blank=True, null=True)
    service_charge_cents = models.IntegerField(blank=True, null=True)
    effective_date_lower = models.DateField(blank=True, null=True)
    effective_date_upper = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    sit_185a_rate_cents = models.IntegerField(blank=True, null=True)
    sit_185b_rate_cents = models.IntegerField(blank=True, null=True)
    sit_pd_schedule = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tariff400ng_service_areas'


class Tariff400NgShorthaulRates(models.Model):
    id = models.UUIDField(primary_key=True)
    cwt_miles_lower = models.IntegerField(blank=True, null=True)
    cwt_miles_upper = models.IntegerField(blank=True, null=True)
    rate_cents = models.IntegerField(blank=True, null=True)
    effective_date_lower = models.DateField(blank=True, null=True)
    effective_date_upper = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tariff400ng_shorthaul_rates'


class Tariff400NgZip3S(models.Model):
    id = models.UUIDField(primary_key=True)
    zip3 = models.CharField(max_length=3, blank=True, null=True)
    basepoint_city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    service_area = models.TextField(blank=True, null=True)
    rate_area = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tariff400ng_zip3s'


class Tariff400NgZip5RateAreas(models.Model):
    id = models.UUIDField(primary_key=True)
    zip5 = models.CharField(max_length=5, blank=True, null=True)
    rate_area = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tariff400ng_zip5_rate_areas'


class TrafficDistributionLists(models.Model):
    id = models.UUIDField(primary_key=True)
    source_rate_area = models.CharField(max_length=255)
    destination_region = models.CharField(max_length=255)
    code_of_service = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'traffic_distribution_lists'
        unique_together = (('source_rate_area', 'destination_region', 'code_of_service'),)


class TransportationOffices(models.Model):
    id = models.UUIDField(primary_key=True)
    shipping_office = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.TextField()
    address = models.ForeignKey(Addresses, models.DO_NOTHING)
    latitude = models.FloatField()
    longitude = models.FloatField()
    hours = models.TextField(blank=True, null=True)
    services = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    gbloc = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'transportation_offices'


class TransportationServiceProviderPerformances(models.Model):
    id = models.UUIDField(primary_key=True)
    performance_period_start = models.DateField()
    performance_period_end = models.DateField()
    traffic_distribution_list = models.ForeignKey(TrafficDistributionLists, models.DO_NOTHING)
    quality_band = models.IntegerField(blank=True, null=True)
    offer_count = models.IntegerField()
    best_value_score = models.FloatField()
    transportation_service_provider = models.ForeignKey('TransportationServiceProviders', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    rate_cycle_start = models.DateField()
    rate_cycle_end = models.DateField()
    linehaul_rate = models.DecimalField(max_digits=65535, decimal_places=65535)
    sit_rate = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'transportation_service_provider_performances'


class TransportationServiceProviders(models.Model):
    id = models.UUIDField(primary_key=True)
    standard_carrier_alpha_code = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    enrolled = models.BooleanField()
    name = models.TextField(blank=True, null=True)
    supplier_id = models.TextField(blank=True, null=True)
    poc_general_name = models.TextField(blank=True, null=True)
    poc_general_email = models.TextField(blank=True, null=True)
    poc_general_phone = models.TextField(blank=True, null=True)
    poc_claims_name = models.TextField(blank=True, null=True)
    poc_claims_email = models.TextField(blank=True, null=True)
    poc_claims_phone = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transportation_service_providers'


class TspUsers(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    last_name = models.TextField()
    first_name = models.TextField()
    middle_initials = models.TextField(blank=True, null=True)
    email = models.TextField(unique=True)
    telephone = models.TextField()
    transportation_service_provider = models.ForeignKey(TransportationServiceProviders, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tsp_users'


class Uploads(models.Model):
    id = models.UUIDField(primary_key=True)
    document = models.ForeignKey(Documents, models.DO_NOTHING, blank=True, null=True)
    uploader = models.ForeignKey('Users', models.DO_NOTHING)
    filename = models.TextField()
    bytes = models.BigIntegerField()
    content_type = models.TextField()
    checksum = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    storage_key = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uploads'


class Users(models.Model):
    id = models.UUIDField(primary_key=True)
    login_gov_uuid = models.UUIDField(unique=True)
    login_gov_email = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'
