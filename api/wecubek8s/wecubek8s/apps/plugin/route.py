# coding=utf-8

from __future__ import absolute_import

from wecubek8s.apps.plugin import controller


def add_routes(api):
    api.add_route('/kubernetes/v1/deployments/apply', controller.Deployment(action='apply'))
    api.add_route('/kubernetes/v1/deployments/remove', controller.Deployment(action='remove'))
    api.add_route('/kubernetes/v1/services/apply', controller.Service(action='apply'))
    api.add_route('/kubernetes/v1/services/remove', controller.Service(action='remove'))