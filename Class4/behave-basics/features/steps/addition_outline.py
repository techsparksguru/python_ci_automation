from behave import *

use_step_matcher('re')

@given("I have two integers (?P<integerA>.+) and (?P<integerB>.+)")
def step_impl(context, integerA, integerB):
    context.integerA = int(integerA)
    context.integerB = int(integerB)

@when("I add the two numbers")
def step_impl(context):
    context.result = int(context.integerA) + int(context.integerB)

@then("The resultant is (?P<result>.+)")
def step_impl(context, result):
    print("Sum of", context.integerA, "and", context.integerB, "is:",context.result)
    assert int(result)==context.result
