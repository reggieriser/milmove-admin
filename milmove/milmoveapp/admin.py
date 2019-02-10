from django.contrib import admin
from .models import Addresses, BackupContacts, BlackoutDates, ClientCerts, Documents, DpsUsers, DutyStations, \
    FuelEiaDieselPrices, GblNumberTrackers, InvoiceNumberTrackers, Invoices, MoveDocuments, Moves, \
    MovingExpenseDocuments, OfficeEmails, OfficePhoneLines, OfficeUsers, Orders, PersonallyProcuredMoves, \
    Reimbursements, SchemaMigration, ServiceAgents, ServiceMembers, ShipmentLineItems, ShipmentOffers, Shipments, \
    SignedCertifications, SocialSecurityNumbers, Tariff400NgFullPackRates, Tariff400NgFullUnpackRates, \
    Tariff400NgItemRates, Tariff400NgItems, Tariff400NgLinehaulRates, Tariff400NgServiceAreas, \
    Tariff400NgShorthaulRates, Tariff400NgZip3S, Tariff400NgZip5RateAreas, TrafficDistributionLists, \
    TransportationOffices, TransportationServiceProviderPerformances, TransportationServiceProviders, TspUsers, Uploads, \
    Users

# Register your models here.
admin.site.register(Addresses)
admin.site.register(BackupContacts)
admin.site.register(BlackoutDates)
admin.site.register(ClientCerts)
admin.site.register(Documents)
admin.site.register(DpsUsers)
admin.site.register(DutyStations)
admin.site.register(FuelEiaDieselPrices)
admin.site.register(GblNumberTrackers)
admin.site.register(InvoiceNumberTrackers)
admin.site.register(Invoices)
admin.site.register(MoveDocuments)
admin.site.register(MovingExpenseDocuments)
admin.site.register(OfficeEmails)
admin.site.register(OfficePhoneLines)
admin.site.register(OfficeUsers)
admin.site.register(Orders)
admin.site.register(PersonallyProcuredMoves)
admin.site.register(Reimbursements)
admin.site.register(SchemaMigration)
admin.site.register(ServiceAgents)
admin.site.register(ServiceMembers)
admin.site.register(ShipmentLineItems)
admin.site.register(ShipmentOffers)
admin.site.register(Shipments)
admin.site.register(SignedCertifications)
admin.site.register(SocialSecurityNumbers)
admin.site.register(Tariff400NgFullPackRates)
admin.site.register(Tariff400NgFullUnpackRates)
admin.site.register(Tariff400NgItemRates)
admin.site.register(Tariff400NgItems)
admin.site.register(Tariff400NgLinehaulRates)
admin.site.register(Tariff400NgServiceAreas)
admin.site.register(Tariff400NgShorthaulRates)
admin.site.register(Tariff400NgZip3S)
admin.site.register(Tariff400NgZip5RateAreas)
admin.site.register(TrafficDistributionLists)
admin.site.register(TransportationOffices)
admin.site.register(TransportationServiceProviderPerformances)
admin.site.register(TransportationServiceProviders)
admin.site.register(TspUsers)
admin.site.register(Uploads)
admin.site.register(Users)


@admin.register(Moves)
class MovesAdmin(admin.ModelAdmin):
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    list_filter = ('selected_move_type', 'status')
    list_display = ('locator', 'orders', 'selected_move_type', 'status', 'created_at')
    readonly_fields = ('id', 'locator', 'created_at', 'updated_at')
    fields = ('id', 'locator', 'orders', 'selected_move_type', 'status', 'cancel_reason', 'created_at', 'updated_at')
