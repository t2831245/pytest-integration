import random
import string
import os
from datetime import date

class Order:
    def __init__(self):
        self.existingAccountNumber = os.getenv("ZUORA_TEST_ACCOUNT")
        self.description = "This is a api test for integration test"
        self.subscriptions = [
            {
                "orderActions": [
                    {
                        "type": "CreateSubscription",
                        "createSubscription": {
                            "subscriptionNumber": self.generate_subscription_number(),
                            "subscribeToProducts": [
                                {
                                    "productRatePlanId": "8ac68cea8aad0fb8018ab1a1a912520d"
                                }
                            ],
                            "terms": {
                                "autoRenew": False,
                                "renewalSetting": "RENEW_WITH_SPECIFIC_TERM",
                                "initialTerm": {
                                    "period": 12,
                                    "periodType": "Month",
                                    "startDate": str(date.today()),
                                    "termType": "TERMED"
                                },
                                "renewalTerms": [
                                    {
                                        "period": 12,
                                        "periodType": "Month"
                                    }
                                ]
                            }
                        },
                        "triggerDates": [
                            {
                                "name": "ContractEffective",
                                "triggerDate": str(date.today()),
                            }
                        ]
                    }
                ],
                "customFields": {
                    "AdminEmail__c": self.generate_adminEmail(),
                    "ServiceRegion__c": "TAIWAN",
                    "UsageRateUnit__c": "minute",
                    "Subdomain__c": self.generate_subDomain(),
                    "PartnerId__c": "m800",
                    "isTesting__c": "Y"
                }
            }
        ]
        self.orderNumber = self.generate_order_number()
        self.orderDate = str(date.today())

    def generate_order_number(self):
        random_numbers = ''.join(random.choice(string.digits) for _ in range(4))
        return f"O-IT-{random_numbers}"


    def generate_subscription_number(self):
        letters = string.ascii_uppercase
        random_letters = ''.join(random.choice(letters) for _ in range(3))
        random_numbers = ''.join(random.choice(string.digits) for _ in range(4))
        return f"IT-{random_letters}-{random_numbers}"

    def generate_adminEmail(self):
        letters = string.ascii_lowercase
        random_letters = ''.join(random.choice(letters) for _ in range(3))
        random_numbers = ''.join(random.choice(string.digits) for _ in range(6))
        return f"it-{random_letters}+{random_numbers}@m800.com"
    
    def generate_subDomain(self):
        letters = string.ascii_lowercase
        random_letters = ''.join(random.choice(letters) for _ in range(3))
        random_numbers = ''.join(random.choice(string.digits) for _ in range(6))
        return f"it-{random_letters}-{random_numbers}"