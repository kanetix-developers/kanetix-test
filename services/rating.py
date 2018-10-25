import operator
import json
from random import randint
import xmltodict

class RatingService(object):

    def get_rates(self):

        rates = {
            '1': 1021,
            '2': 1245,
            '3': 2353
        }

        rates['4'] = self._get_rate_for_id4()
        rates['5'] = self._get_rate_for_id5()

        # remove any zero rates, no point displaying them
        final_rates = dict()
        for company_id in rates:
            if rates[company_id]:
                final_rates[company_id] = rates[company_id]

        # return sorted by rate
        return sorted(final_rates.items(), key=operator.itemgetter(1))

    def _get_rate_for_id4(self):

        response = self._fake_api_call1()
        xml = xmltodict.parse(response)

        rate = 0

        try:
            for coverage in xml['soap:Envelope']['soap:Body']['ExecuteResponse']['Response']['ExecuteResult']['AutoQuoteListRs']['AutoQuoteRs']['VehicleListRs']['VehicleRs']['CoverageListRs']['CoverageRs']:
                rate = rate + int(coverage['BaseAmount'])
        except:
            pass

        return rate


    def _get_rate_for_id5(self):

        json_response = self._fake_api_call2()


        response = json.loads(json_response)

        rate = 0
        if response['status'] == 1:
            rate = response['premium']

        return rate

    def _fake_api_call1(self):
        ''' this is a mocked method, do not modify '''
        return '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><ExecuteResponse xmlns="http://acmecorpupload"><ExecuteResult><TransactionReqId>KA180214-VGPTX_103729</TransactionReqId><AutoQuoteListRs><AutoQuoteRs><AppReqId>KA180214-VGPTX</AppReqId><RateControlNumber>14</RateControlNumber><DiscountsSurchargesApplied>0</DiscountsSurchargesApplied><TakeTwoSavings>0</TakeTwoSavings><CltvScoreBand>C</CltvScoreBand><CltvScore>-737</CltvScore><CltvIndicator>1</CltvIndicator><VehicleListRs><VehicleRs><VehicleId>202420</VehicleId><IAOCode>1632</IAOCode><RateClassCode>A140A011900131000310</RateClassCode><RiskPointCalculatorScore>3</RiskPointCalculatorScore><AntitheftDeviceRequiredIndicator>0</AntitheftDeviceRequiredIndicator><VehicleCltvScore>-737</VehicleCltvScore><ClaimForgivenessEligibility>false</ClaimForgivenessEligibility><FeaturesApplied>0</FeaturesApplied><IsDriverId>100948744</IsDriverId><DiscountListRs><DiscountRs><Code>PK</Code><Amount>10.00</Amount><Unit>PCT</Unit></DiscountRs><DiscountRs><Code>RN</Code><Amount>2.00</Amount><Unit>PCT</Unit></DiscountRs><DiscountRs><Code>WT</Code><Amount>5.00</Amount><Unit>PCT</Unit></DiscountRs></DiscountListRs><CoverageListRs><CoverageRs><CoverageTypeCode>CV</CoverageTypeCode><CoverageCode>PD</CoverageCode><CoverageLimit>0</CoverageLimit><CoverageDeductible>0</CoverageDeductible><BasePremium>343</BasePremium></CoverageRs><CoverageRs><CoverageTypeCode>CV</CoverageTypeCode><CoverageCode>UM</CoverageCode><CoverageLimit>200000</CoverageLimit><CoverageDeductible>0</CoverageDeductible><BasePremium>18</BasePremium></CoverageRs><CoverageRs><CoverageTypeCode>CV</CoverageTypeCode><CoverageCode>BI</CoverageCode><CoverageLimit>1000000</CoverageLimit><CoverageDeductible>0</CoverageDeductible><BasePremium>569</BasePremium></CoverageRs><CoverageRs><CoverageTypeCode>CV</CoverageTypeCode><CoverageCode>MR</CoverageCode><CoverageLimit>65000</CoverageLimit><CoverageDeductible>0</CoverageDeductible><BasePremium>183</BasePremium></CoverageRs><CoverageRs><CoverageTypeCode>CV</CoverageTypeCode><CoverageCode>IR</CoverageCode><CoverageLimit>400</CoverageLimit><CoverageDeductible>0</CoverageDeductible><BasePremium>46</BasePremium></CoverageRs><CoverageRs><CoverageTypeCode>CV</CoverageTypeCode><CoverageCode>DB</CoverageCode><CoverageLimit>25000</CoverageLimit><CoverageDeductible>0</CoverageDeductible><BasePremium>4</BasePremium></CoverageRs><CoverageRs><CoverageTypeCode>CV</CoverageTypeCode><CoverageCode>FB</CoverageCode><CoverageLimit>6000</CoverageLimit><CoverageDeductible>0</CoverageDeductible><BasePremium>3</BasePremium></CoverageRs><CoverageRs><CoverageTypeCode>CV</CoverageTypeCode><CoverageCode>CB</CoverageCode><CoverageLimit>0</CoverageLimit><CoverageDeductible>0</CoverageDeductible><BasePremium>0</BasePremium></CoverageRs><CoverageRs><CoverageTypeCode>CV</CoverageTypeCode><CoverageCode>DC</CoverageCode><CoverageLimit>0</CoverageLimit><CoverageDeductible>0</CoverageDeductible><BasePremium>0</BasePremium></CoverageRs><CoverageRs><CoverageTypeCode>CV</CoverageTypeCode><CoverageCode>CM</CoverageCode><CoverageLimit>0</CoverageLimit><CoverageDeductible>1000</CoverageDeductible><BasePremium>54</BasePremium></CoverageRs><CoverageRs><CoverageTypeCode>CV</CoverageTypeCode><CoverageCode>CL</CoverageCode><CoverageLimit>0</CoverageLimit><CoverageDeductible>1000</CoverageDeductible><BasePremium>267</BasePremium></CoverageRs><CoverageRs><CoverageTypeCode>FM</CoverageTypeCode><CoverageCode>44R</CoverageCode><CoverageLimit>1000000</CoverageLimit><CoverageDeductible>0</CoverageDeductible><BasePremium>17</BasePremium></CoverageRs></CoverageListRs></VehicleRs></VehicleListRs></AutoQuoteRs></AutoQuoteListRs></ExecuteResult></ExecuteResponse></soap:Body></soap:Envelope>'


    def _fake_api_call2(self):
        ''' this is mocked method, do not modify '''
        if randint(0, 3) == 2:
            return '{ "status": 0, "error": "server unavailable, try again" }'
        return '{ "status": 1, "premium": 914 } '
