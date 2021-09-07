"""
Copyright 2020 Lightbend Inc.
Licensed under the Apache License, Version 2.0.
"""
from akkaserverless.action_context import ActionContext
from akkaserverless.action_protocol_entity import Action
from api_action_pb2 import (MyRequest, MyResponse, _MYACTIONSERVICE, DESCRIPTOR as API_DESCRIPTOR)

action = Action(_MYACTIONSERVICE, [API_DESCRIPTOR])

@action.unary_handler("Hello")
def hello(command: MyRequest, context: ActionContext):
    return MyResponse(text= "Do you want to play a game, " + command.name + "?")