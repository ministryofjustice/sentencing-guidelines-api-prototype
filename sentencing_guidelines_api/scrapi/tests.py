from django.test import TestCase
from sentencing_guidelines_api.scrapi.management.commands._offences import OffenceScraper
from unittest.mock import MagicMock


# Create your tests here.
class ScrapiTestCase(TestCase):
    LIST_OF_OFFENCES_MARKUP = ''' <ul class="offences-filter-list">
	<li>
		<div class="hgroup"><h4></h4><h4><a href="/offences/magistrates-court/item/abstracting-electricity" title="Theft">Theft</a></h4></div><div>
		<div class="offence-acts">Theft Act 1968, s.13</div><div class="offence-tags">evasion,illegal,s.13,s13,section 13,theft,</div>
					</div>
	</li>
	<li>
		<div class="hgroup"><h4></h4><h4><a href="/offences/magistrates-court/item/abstracting-electricity" title="Murder">Murder</a></h4></div><div>
		<div class="offence-acts">Theft Act 1968, s.13</div><div class="offence-tags">evasion,illegal,s.13,s13,section 13,theft,</div>
					</div>
	</li>
	<li>
		<div class="hgroup"><h4></h4><h4><a href="/offences/magistrates-court/item/abstracting-electricity" title="Fraud">Fraud</a></h4></div><div>
		<div class="offence-acts">Theft Act 1968, s.13</div><div class="offence-tags">evasion,illegal,s.13,s13,section 13,theft,</div>
					</div>
	</li>
</ul>'''
    def setUp(self):
        self.offences = ['Theft', 'Murder', 'Fraud']
        self.scraper = OffenceScraper()
        self.scraper.get_list_of_offences_markup = MagicMock(return_value = self.LIST_OF_OFFENCES_MARKUP)

    def test_get_offences_list(self):
        self.assertListEqual(self.scraper.get_list_of_offences(), self.offences )

