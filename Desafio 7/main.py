from api.models import User, Agent, Event, Group
from datetime import date, timedelta


def get_active_users() -> User:
    """Traga todos os uarios ativos,
    seu último login deve ser menor que 10 dias """
    limit = date.today() - timedelta(days=10)
    queryset = User.objects.filter(last_login__gt=limit)
    return queryset


def get_amount_users() -> User:
    """Retorne a quantidade total de usuarios do sistema """
    total = User.objects.count()
    return total


def get_admin_users() -> User:
    """Traga todos os usuarios com grupo = 'admin"""
    queryset = User.objects.filter(group__name="admin")
    return queryset


def get_all_debug_events() -> Event:
    """Traga todos os eventos com tipo debug"""
    queryset = Event.objects.filter(level="debug")
    return queryset


def get_all_critical_events_by_user(agent) -> Event:
    """Traga todos os eventos do tipo critico de um usuário específico"""
    queryset = Event.objects.filter(level="critical", agent=agent)
    return queryset


def get_all_agents_by_user(username) -> Agent:
    """Traga todos os agentes de associados a um usuário pelo nome"""
    queryset = Agent.objects.filter(user__name=username)
    return queryset


def get_all_events_by_group() -> Group:
    """Traga todos os grupos que contenham alguem que possua um agente
    que possuem eventos do tipo information"""
    queryset = Group.objects.filter(user__agent__event__level="information")
    return queryset
