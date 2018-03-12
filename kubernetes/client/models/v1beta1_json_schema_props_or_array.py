# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1JSONSchemaPropsOrArray(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'json_schemas': 'list[V1beta1JSONSchemaProps]',
        'schema': 'V1beta1JSONSchemaProps'
    }

    attribute_map = {
        'json_schemas': 'JSONSchemas',
        'schema': 'Schema'
    }

    def __init__(self, json_schemas=None, schema=None):
        """
        V1beta1JSONSchemaPropsOrArray - a model defined in Swagger
        """

        self._json_schemas = None
        self._schema = None
        self.discriminator = None

        self.json_schemas = json_schemas
        self.schema = schema

    @property
    def json_schemas(self):
        """
        Gets the json_schemas of this V1beta1JSONSchemaPropsOrArray.

        :return: The json_schemas of this V1beta1JSONSchemaPropsOrArray.
        :rtype: list[V1beta1JSONSchemaProps]
        """
        return self._json_schemas

    @json_schemas.setter
    def json_schemas(self, json_schemas):
        """
        Sets the json_schemas of this V1beta1JSONSchemaPropsOrArray.

        :param json_schemas: The json_schemas of this V1beta1JSONSchemaPropsOrArray.
        :type: list[V1beta1JSONSchemaProps]
        """
        if json_schemas is None:
            raise ValueError("Invalid value for `json_schemas`, must not be `None`")

        self._json_schemas = json_schemas

    @property
    def schema(self):
        """
        Gets the schema of this V1beta1JSONSchemaPropsOrArray.

        :return: The schema of this V1beta1JSONSchemaPropsOrArray.
        :rtype: V1beta1JSONSchemaProps
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the schema of this V1beta1JSONSchemaPropsOrArray.

        :param schema: The schema of this V1beta1JSONSchemaPropsOrArray.
        :type: V1beta1JSONSchemaProps
        """
        if schema is None:
            raise ValueError("Invalid value for `schema`, must not be `None`")

        self._schema = schema

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1beta1JSONSchemaPropsOrArray):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
