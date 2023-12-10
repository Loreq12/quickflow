import pytest

from quickflow.external_actions.strategy import AVAILABLE_MODULES, BASE_STRATEGIES
from quickflow.external_actions.strategy.base import AbstractServiceStrategy, AbstractAction


@pytest.mark.dependency()
def test_if_strategy_mapper_is_implemented():
    for _, strategies in AVAILABLE_MODULES.items():
        for strategy_name, strategy_class in strategies.items():
            try:
                assert type(strategy_class().get_action_to_function_mapper()) == dict, f"{strategy_class.module_name=} is not properly initialized. Missing mapping between actions and functions"
            except NotImplementedError:
                assert False, f"{strategy_name=} is not properly initialized. Mapping was not defined for 'get_action_to_function_mapper' method"


@pytest.mark.dependency()
def test_if_base_strategy_have_action_assigned():
    for strategy_class in BASE_STRATEGIES:
        assert strategy_class.actions != AbstractAction, f"{strategy_class.__name__} class does not have proper action overloaded."


@pytest.mark.dependency(depends=["test_if_strategy_mapper_is_implemented", "test_if_base_strategy_have_action_assigned"])
def test_if_all_actions_are_mapped_to_function_calls():
    for _, strategies in AVAILABLE_MODULES.items():
        for strategy_name, strategy_class in strategies.items():
            strategy: AbstractServiceStrategy = strategy_class()
            assert len(strategy.get_action_to_function_mapper().keys()) == len(strategy.actions)
