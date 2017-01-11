Feature: greet hello world

  Scenario: greeter respond hello world
    When service alive
    Then greet hello world when calling api

  Scenario: greeter respond hello world by name
    When service alive
    Then greet personally given myname

  @clock
  Scenario: greeter respond zzz between 14 and 16
    When service alive
    Then greet zzz when clock between 14 and 16