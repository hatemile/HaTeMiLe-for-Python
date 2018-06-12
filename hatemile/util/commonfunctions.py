# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re


class CommonFunctions:
    """
    The CommonFuncionts class contains the used methods by HaTeMiLe classes.
    """

    count = 0

    @staticmethod
    def generate_id(element, prefix):
        """
        Generate a id for a element.

        :param element: The element.
        :type element: hatemile.util.htmldomelement.HTMLDOMElement
        :param prefix: The prefix of id.
        :type prefix: str
        """

        if not element.has_attribute('id'):
            element.set_attribute('id', prefix + str(CommonFunctions.count))
            CommonFunctions.count += 1

    @staticmethod
    def reset_count():
        """
        Reset the count number of ids.
        """

        CommonFunctions.count = 0

    @staticmethod
    def set_list_attributes(element1, element2, attributes):
        """
        Copy a list of attributes of a element for other element.

        :param element1: The element that have attributes copied.
        :type element1: hatemile.util.htmldomelement.HTMLDOMElement
        :param element2: The element that copy the attributes.
        :type element2: hatemile.util.htmldomelement.HTMLDOMElement
        :param attributes: The list of attributes that will be copied.
        :type attributes: list(str)
        """

        for attribute in attributes:
            if element1.has_attribute(attribute):
                element2.set_attribute(
                    attribute,
                    element1.get_attribute(attribute)
                )

    @staticmethod
    def increase_in_list(list_to_increase, string_to_increase):
        """
        The list of attributes that will be copied.

        :param list_to_increase: The list.
        :type list_to_increase: str
        :param string_to_increase: The value of item.
        :type string_to_increase: str
        :return: The list with the item added, if the item not was contained in
        list.
        :rtype: str
        """

        if (bool(list_to_increase)) and (bool(string_to_increase)):
            if CommonFunctions.in_list(list_to_increase, string_to_increase):
                return list_to_increase
            return list_to_increase + ' ' + string_to_increase
        elif bool(list_to_increase):
            return list_to_increase
        return string_to_increase

    @staticmethod
    def in_list(list_to_search, string_to_search):
        """
        Verify if the list contains the item.

        :param list_to_search: The list.
        :type list_to_search: str
        :param string_to_search: The value of item.
        :type string_to_search: str
        :return: True if the list contains the item or false is not contains.
        :rtype: bool
        """

        if (bool(list_to_search)) and (bool(string_to_search)):
            elements = re.split('[ \n\t\r]+', list_to_search)
            for element in elements:
                if element == string_to_search:
                    return True
        return False
