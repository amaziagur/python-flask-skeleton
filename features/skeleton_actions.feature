Feature: greet hello world

  Scenario: greeter respond hello world
    When service alive
    Then greet hello world when calling api