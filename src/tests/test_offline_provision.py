import os
import sys
import time
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from model.zuora_api import *
from model.order import Order
from common.create_subscription import create_subscription
from common.get_subscription import get_subscription
from common.delete_subcription import delete_subcription
from common.get_order import get_orde_not_found


class TestOfflineProvision:
    @pytest.fixture(scope="class")
    def order_instance(self):
        return Order()

    def test_base_provision(self, zuora_header, order_instance):
        create_subscription(zuora_header, order_instance)
        time.sleep(5)
        get_subscription(zuora_header, order_instance)
        delete_subcription(zuora_header, order_instance)
        time.sleep(5)
        get_orde_not_found(zuora_header, order_instance.orderNumber)

    def test_update_provision(self):
        pass

    def test_base_addon_provsion(self):
        pass
