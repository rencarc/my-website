from oscar.core.loading import get_class

try:
    OfferApplications = get_class('offer.results', 'OfferApplications')
    print("Module loaded successfully:", OfferApplications)
except Exception as e:
    print("Error loading module:", str(e))