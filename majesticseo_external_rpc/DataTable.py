
# Copyright 2019, Majestic-12 Ltd trading as Majestic
# https://majestic.com
# 
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
# 
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
# 
#     * Neither the name of Majestic-12 Ltd, its trademarks, nor any contributors
#       to the software may be used to endorse or promote products derived from
#       this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Majestic-12 Ltd BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import re

class DataTable:

    def __init__(self):
        """ This constructs a new instance of the DataTable module. """
        self.name = ''
        self.headers = []
        self.params = {}
        self.rows = []


    def set_table_name(self, name):
        """ Set table's name """
        self.name = name


    def set_table_headers(self, headers):
        """ Set table's headers """
        self.headers = self.__split(headers)


    def set_table_params(self, name, value):
        """ Set table's parameters """
        self.params[name] = value


    def set_table_row(self, row):
        """ Set table's rows """
        rows_hash = {}
        elements = self.__split(row) 
        for index, element in enumerate(elements):
            if(element == ' '):
                element = ''
            rows_hash[self.headers[index]] = element
        self.rows.append(rows_hash)


    def __split(self, value):
        # Splits the input from pipe separated form into an array.
        regex = re.compile('(?<!\|)\|(?!\|)')
        array = regex.split(value)
        for index, item in enumerate(array):
            array[index] = item.replace('||', '|')
        return array


    def get_param_for_name(self, name):
        """ Returns a table's parameter for a given name """
        if(name in self.params):
            return self.params[name]
        return None

    def get_row_count(self):
        """ Returns the number of rows in the table """
        return len(self.rows)