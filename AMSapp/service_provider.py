from dependency_injector import containers, providers
from AMSapp.repositories.AccountHolderRepository import AccountHolderRepository, DjangoORMAccountHolderRepository
from AMSapp.services.AccountHolderManagementService import AccountHolderManagementService, \
    DefaultAccountHolderManagementService
from AMSapp.repositories.ManagerRepository import ManagerRepository, DjangoORMManagerRepository
from AMSapp.services.ManagerManagementService import ManagerManagementService, \
    DefaultManagerManagementService
from AMSapp.repositories.AccountRepository import AccountRepository, DjangoORMAccountRepository
from AMSapp.services.AccountManagementService import AccountManagementService, DefaultAccountManagementService
from AMSapp.repositories.LoanRepository import LoanRepository, DjangoORMLoanRepository
from AMSapp.services.LoanManagementService import LoanManagementServices, DefaultLoanManagementServices
from AMSapp.repositories.OverdraftRepository import OverdraftRepository, DjangoORMOverdraftOverdraft
from AMSapp.services.OverdraftManagementService import OverdraftManagementService, DefaultOverdraftManagementService
from typing import Callable


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    account_holder_repository: Callable[[], AccountHolderRepository] = providers.Factory(
        DjangoORMAccountHolderRepository
    )

    account_holder_management_service: Callable[[], AccountHolderManagementService] = providers.Factory(
        DefaultAccountHolderManagementService,
        repository=account_holder_repository
    )

    manager_repository: Callable[[], ManagerRepository] = providers.Factory(
        DjangoORMManagerRepository
    )

    manager_management_service: Callable[[], ManagerManagementService] = providers.Factory(
        DefaultManagerManagementService,
        repository=manager_repository
    )

    account_repository: Callable[[], AccountRepository] = providers.Factory(
        DjangoORMAccountRepository
    )

    account_management_service: Callable[[], AccountManagementService] = providers.Factory(
        DefaultAccountManagementService, repository=account_repository
    )

    loan_repository: Callable[[], LoanRepository] = providers.Factory(
        DjangoORMLoanRepository
    )

    loan_management_service: Callable[[], LoanManagementServices] = providers.Factory(
        DefaultLoanManagementServices, repository=loan_repository
    )

    overdraft_repository: Callable[[], OverdraftRepository] = providers.Factory(
        DjangoORMOverdraftOverdraft
    )

    overdraft_management_service: Callable[[], OverdraftManagementService] = providers.Factory(
        DefaultOverdraftManagementService, repository=overdraft_repository
    )


ams_service_provider = Container()
