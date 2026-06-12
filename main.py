from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from utils.settings import settings
from commands.router import CommandRouter
from memory.database import Database

from agents.director_agent import DirectorAgent
from agents.pricing_agent import PricingAgent



from memory.context_manager import (
    ContextManager
)

from memory.history_manager import (
    HistoryManager
)

from memory.client_manager import (
    ClientManager
)

from memory.client_scoring import (
    ClientScoring
)

from memory.service_recommendation import (
    ServiceRecommendationEngine
)

from memory.crm_manager import (
    CRMManager
)

from memory.scheduler_manager import (
    SchedulerManager
)

from memory.automation_manager import (
    AutomationManager
)

from models.project_context import (
    ProjectContext
)

from utils.currency_formatter import (
    CurrencyFormatter
)

from memory.sales_manager import (
    SalesManager
)

console = Console()


def print_header():

    console.print()

    console.print(
        Panel.fit(
            "[bold cyan]DESIGN OS[/bold cyan]\n"
            "Autonomous Design Assistant",
            border_style="cyan"
        )
    )

    console.print()


def show_pricing(pricing):

    local_table = Table(
        title="Harga Lokal"
    )

    local_table.add_column(
        "Paket"
    )

    local_table.add_column(
        "Harga"
    )

    local_table.add_row(
        "Basic",
        CurrencyFormatter.idr(
            pricing.local_price["basic"]
        )
    )

    local_table.add_row(
        "Standard",
        CurrencyFormatter.idr(
            pricing.local_price["standard"]
        )
    )

    local_table.add_row(
        "Premium",
        CurrencyFormatter.idr(
            pricing.local_price["premium"]
        )
    )

    console.print(
        local_table
    )

    international_table = Table(
        title="Harga Internasional"
    )

    international_table.add_column(
        "Paket"
    )

    international_table.add_column(
        "Harga"
    )

    international_table.add_row(
        "Basic",
        CurrencyFormatter.usd(
            pricing.international_price[
                "basic"
            ]
        )
    )

    international_table.add_row(
        "Standard",
        CurrencyFormatter.usd(
            pricing.international_price[
                "standard"
            ]
        )
    )

    international_table.add_row(
        "Premium",
        CurrencyFormatter.usd(
            pricing.international_price[
                "premium"
            ]
        )
    )

    console.print(
        international_table
    )

    summary = Table(
        title="Rekomendasi Harga"
    )

    summary.add_column(
        "Item"
    )

    summary.add_column(
        "Nilai"
    )

    summary.add_row(
        "Segment",
        pricing.market_segment
    )

    summary.add_row(
        "Complexity Score",
        str(
            pricing.complexity_score
        )
    )

    summary.add_row(
        "Recommended Package",
        pricing.recommended_package
    )

    summary.add_row(
        "Negotiation Floor",
        CurrencyFormatter.idr(
            pricing.negotiation_floor
        )
    )

    summary.add_row(
        "Target Price",
        CurrencyFormatter.idr(
            pricing.target_price
        )
    )

    summary.add_row(
        "Ceiling Price",
        CurrencyFormatter.idr(
            pricing.ceiling_price
        )
    )

    console.print(
        summary
    )


def show_analytics(
    analytics
):

    console.print()

    console.print(
        Panel(
            f"Total Projects : {analytics['total_projects']}",
            title="Analytics",
            border_style="cyan"
        )
    )

    workflow_table = Table(
        title="Top Workflows"
    )

    workflow_table.add_column(
        "Workflow"
    )

    workflow_table.add_column(
        "Count"
    )

    for workflow, count in analytics[
        "top_workflows"
    ]:

        workflow_table.add_row(
            str(workflow),
            str(count)
        )

    console.print(
        workflow_table
    )

    project_table = Table(
        title="Top Project Types"
    )

    project_table.add_column(
        "Project Type"
    )

    project_table.add_column(
        "Count"
    )

    for project_type, count in analytics[
        "top_project_types"
    ]:

        project_table.add_row(
            str(project_type),
            str(count)
        )

    console.print(
        project_table
    )

    category_table = Table(
        title="Top Categories"
    )

    category_table.add_column(
        "Category"
    )

    category_table.add_column(
        "Count"
    )

    for category, count in analytics[
        "top_categories"
    ]:

        category_table.add_row(
            str(category),
            str(count)
        )

    console.print(
        category_table
    )

    console.print()


def show_client(
    client,
    projects,
    intelligence,
    notes
):

    table = Table(
        title=f"Client : {client[0]}"
    )

    table.add_column(
        "Field"
    )

    table.add_column(
        "Value"
    )

    table.add_row(
        "Country",
        str(client[1])
    )

    table.add_row(
        "Industry",
        str(client[2])
    )

    table.add_row(
        "Notes",
        str(client[3])
    )

    table.add_row(
        "Projects",
        str(
            intelligence[
                "total_projects"
            ]
        )
    )

    table.add_row(
        "Unique Projects",
        str(
            intelligence[
                "unique_projects"
            ]
        )
    )

    table.add_row(
        "Preferred Category",
        intelligence[
            "preferred_category"
        ]
    )

    table.add_row(
        "Most Used Workflow",
        intelligence[
            "most_used_workflow"
        ]
    )

    table.add_row(
        "First Seen",
        intelligence[
            "first_seen"
        ]
    )

    table.add_row(
        "Last Seen",
        intelligence[
            "last_seen"
        ]
    )

    console.print(
        table
    )

    if projects:

        project_table = Table(
            title="Recent Projects"
        )

        project_table.add_column(
            "Brief"
        )

        project_table.add_column(
            "Workflow"
        )

        project_table.add_column(
            "Category"
        )

        for project in projects[:10]:

            project_table.add_row(
                str(project[0]),
                str(project[1]),
                str(project[2])
            )

        console.print(
            project_table
        )

    if intelligence[
        "top_tags"
    ]:

        tag_table = Table(
            title="Top Tags"
        )

        tag_table.add_column(
            "Tag"
        )

        for tag in intelligence[
            "top_tags"
        ]:

            tag_table.add_row(
                tag
            )

        console.print(
            tag_table
        )
        
    console.print()

    if notes:

        note_table = Table(
            title="Client Notes"
        )

        note_table.add_column(
            "Note"
        )

        note_table.add_column(
            "Created"
        )

        for note in notes:

            note_table.add_row(
                str(note[0]),
                str(note[1])
            )

        console.print(
            note_table
        )


def show_recommendations(
    client_name,
    recommendations
):

    table = Table(
        title=f"Recommended Services : {client_name}"
    )

    table.add_column(
        "Service"
    )

    table.add_column(
        "Score"
    )

    for service, score in recommendations[
        "recommendations"
    ]:

        table.add_row(
            str(service),
            str(score)
        )

    console.print(
        table
    )

    console.print(
        Panel(
            f"Upsell Score : {recommendations['upsell_score']}",
            title="Client Recommendation",
            border_style="green"
        )
    )

    console.print()

def show_client_score(score):

    table = Table(
        title=f"Client Score : {score.client_name}"
    )

    table.add_column(
        "Field"
    )

    table.add_column(
        "Value"
    )

    table.add_row(
        "Score",
        str(score.score)
    )

    table.add_row(
        "Tier",
        score.tier
    )

    table.add_row(
        "Projects",
        str(score.total_projects)
    )

    table.add_row(
        "Categories",
        str(score.category_count)
    )

    table.add_row(
        "Relationship Notes",
        str(score.relationship_notes)
    )

    console.print(
        table
    )

    reason_table = Table(
        title="Scoring Reasons"
    )

    reason_table.add_column(
        "Reason"
    )

    for reason in score.reasons:

        reason_table.add_row(
            reason
        )

    console.print(
        reason_table
    )

    console.print()

def show_service_recommendation(
    recommendation
):

    summary = Table(
        title=f"Service Recommendation : {recommendation.client_name}"
    )

    summary.add_column(
        "Field"
    )

    summary.add_column(
        "Value"
    )

    summary.add_row(
        "Client Score",
        str(
            recommendation.client_score
        )
    )

    summary.add_row(
        "Client Tier",
        recommendation.client_tier
    )

    summary.add_row(
        "Confidence",
        f"{recommendation.confidence_score}%"
    )

    summary.add_row(
        "Upsell",
        (
            "YES"
            if recommendation.upsell_opportunity
            else "NO"
        )
    )

    summary.add_row(
        "Cross-Sell",
        (
            "YES"
            if recommendation.cross_sell_opportunity
            else "NO"
        )
    )

    console.print(
        summary
    )

    table = Table(
        title="Recommended Services"
    )

    table.add_column(
        "Service"
    )

    table.add_column(
        "Score"
    )

    table.add_column(
        "Reason"
    )

    for item in recommendation.recommendations:

        table.add_row(
            item.service,
            str(item.score),
            item.reason
        )

    console.print(
        table
    )

    console.print()

def show_crm_pipeline(
    pipeline
):

    table = Table(
        title=f"CRM Pipeline : {pipeline.client_name}"
    )

    table.add_column(
        "Field"
    )

    table.add_column(
        "Value"
    )

    table.add_row(
        "Status",
        pipeline.status
    )

    table.add_row(
        "Next Action",
        pipeline.next_action
    )

    table.add_row(
        "Projects",
        str(
            pipeline.project_count
        )
    )

    table.add_row(
        "Notes",
        str(
            pipeline.notes_count
        )
    )

    table.add_row(
        "Client Score",
        str(
            pipeline.client_score
        )
    )

    table.add_row(
        "Client Tier",
        pipeline.client_tier
    )

    console.print(
        table
    )

    console.print()

def show_crm_dashboard(
    summary
):

    table = Table(
        title="CRM Dashboard"
    )

    table.add_column(
        "Stage"
    )

    table.add_column(
        "Total"
    )

    for stage, total in (
        summary.items()
    ):

        table.add_row(
            stage,
            str(total)
        )

    console.print(
        table
    )

    console.print()

def show_sales_strategy(
    strategy
):

    table = Table(
        title=f"Sales Intelligence : {strategy.client_name}"
    )

    table.add_column(
        "Field"
    )

    table.add_column(
        "Value"
    )

    table.add_row(
        "Client Score",
        str(
            strategy.client_score
        )
    )

    table.add_row(
        "Client Tier",
        strategy.client_tier
    )

    table.add_row(
        "Closing Probability",
        f"{strategy.closing_probability}%"
    )

    table.add_row(
        "Revenue Potential",
        strategy.revenue_potential
    )

    table.add_row(
        "Priority",
        strategy.priority
    )

    table.add_row(
        "Estimated Revenue",
        f"Rp {strategy.estimated_revenue:,}"
    )

    console.print(
        table
    )

    action_table = Table(
        title="Recommended Actions"
    )

    action_table.add_column(
        "Action"
    )

    for action in (
        strategy.recommended_actions
    ):

        action_table.add_row(
            action
        )

    console.print(
        action_table
    )

    upsell_table = Table(
        title="Upsell Services"
    )

    upsell_table.add_column(
        "Service"
    )

    for service in (
        strategy.upsell_services
    ):

        upsell_table.add_row(
            service
        )

    console.print(
        upsell_table
    )

    console.print()

def show_sales_leaderboard(
    leaderboard
):

    table = Table(
        title="Sales Leaderboard"
    )

    table.add_column(
        "Rank"
    )

    table.add_column(
        "Client"
    )

    table.add_column(
        "Tier"
    )

    table.add_column(
        "Priority"
    )

    table.add_column(
        "Close %"
    )

    table.add_column(
        "Revenue"
    )

    for index, item in enumerate(
        leaderboard,
        start=1
    ):

        table.add_row(

            str(index),

            item.client_name,

            item.client_tier,

            item.priority,

            str(
                item.closing_probability
            ),

            f"Rp {item.estimated_revenue:,}"
        )

    console.print(
        table
    )

    console.print()

def show_pipeline_analytics(
    analytics
):

    table = Table(
        title="Sales Pipeline"
    )

    table.add_column(
        "Metric"
    )

    table.add_column(
        "Value"
    )

    table.add_row(
        "Total Pipeline",
        f"Rp {analytics['total_pipeline']:,}"
    )

    table.add_row(
        "Forecast Revenue",
        f"Rp {analytics['forecast_revenue']:,}"
    )

    table.add_row(
        "High Priority Clients",
        str(
            analytics[
                "high_priority"
            ]
        )
    )

    table.add_row(
        "Total Opportunities",
        str(
            analytics[
                "opportunities"
            ]
        )
    )

    console.print(
        table
    )

    console.print()

def show_scheduler_tasks(
    tasks
):

    from rich.table import (
        Table
    )

    table = Table(
        title="Scheduler Tasks"
    )

    table.add_column(
        "ID"
    )

    table.add_column(
        "Title"
    )

    table.add_column(
        "Date"
    )

    table.add_column(
        "Status"
    )

    for task in tasks:

        table.add_row(
            str(task["id"]),
            task["title"],
            task["date"],
            task["status"]
        )

    console.print(
        table
    )

def show_scheduler_dashboard(
    dashboard
):

    table = Table(
        title=
        "Scheduler Dashboard"
    )

    table.add_column(
        "Metric"
    )

    table.add_column(
        "Value"
    )

    table.add_row(
        "Total Tasks",
        str(
            dashboard[
                "total_tasks"
            ]
        )
    )

    table.add_row(
        "Pending Tasks",
        str(
            dashboard[
                "pending_tasks"
            ]
        )
    )

    table.add_row(
        "Completed Tasks",
        str(
            dashboard[
                "completed_tasks"
            ]
        )
    )

    table.add_row(
        "Completion Rate",
        (
            str(
                dashboard[
                    "completion_rate"
                ]
            )
            + "%"
        )
    )

    console.print(
        table
    )

def show_forecast_summary(
    summary
):

    table = Table(
        title="Sales Forecast"
    )

    table.add_column(
        "Priority"
    )

    table.add_column(
        "Revenue"
    )

    total = 0

    for priority in [
        "A",
        "B",
        "C"
    ]:

        revenue = (
            summary[
                priority
            ]
        )

        total += revenue

        table.add_row(
            priority,
            f"Rp {revenue:,}"
        )

    table.add_row(
        "TOTAL",
        f"Rp {total:,}"
    )

    console.print(
        table
    )

    console.print()

def show_opportunities(
    opportunities
):

    table = Table(
        title="Sales Opportunities"
    )

    table.add_column(
        "Client"
    )

    table.add_column(
        "Priority"
    )

    table.add_column(
        "Close %"
    )

    table.add_column(
        "Revenue"
    )

    for item in opportunities:

        table.add_row(
            item.client_name,
            item.priority,
            str(
                item.closing_probability
            ),
            f"Rp {item.estimated_revenue:,}"
        )

    console.print(
        table
    )

    console.print()

def show_pipeline_update_result(
    client_name,
    status
):

    console.print()

    console.print(
        f"[green]Pipeline updated[/green]"
    )

    console.print(
        f"Client : {client_name}"
    )

    console.print(
        f"Status : {status}"
    )

    console.print()

def show_client_ranking(
    ranking
):

    table = Table(
        title="Top Clients"
    )

    table.add_column("Rank")
    table.add_column("Client")
    table.add_column("Score")
    table.add_column("Tier")

    for index, client in enumerate(
        ranking,
        start=1
    ):

        table.add_row(
            str(index),
            client.client_name,
            str(client.score),
            client.tier
        )

    console.print(
        table
    )

    console.print()

def show_automation_dashboard(data):

    from rich.table import Table

    table = Table(
        title="Automation Dashboard"
    )

    table.add_column("Metric")
    table.add_column("Value")

    table.add_row(
        "Total Rules",
        str(data["total_rules"])
    )

    table.add_row(
        "Enabled Rules",
        str(data["enabled_rules"])
    )

    table.add_row(
        "Total Executions",
        str(data["total_executions"])
    )

    console.print(table)

def show_automation_analytics(data):

    from rich.table import Table

    table = Table(
        title="Automation Analytics"
    )

    table.add_column("Metric")
    table.add_column("Value")

    for key, value in data.items():

        table.add_row(
            key.replace("_", " ").title(),
            str(value)
        )

    console.print(table)

def show_automation_report(data):

    from rich.table import Table

    dashboard = data["dashboard"]
    analytics = data["analytics"]

    dashboard_table = Table(
        title="Automation Dashboard"
    )

    dashboard_table.add_column("Metric")
    dashboard_table.add_column("Value")

    for key, value in dashboard.items():

        dashboard_table.add_row(
            key.replace("_", " ").title(),
            str(value)
        )

    console.print(dashboard_table)

    analytics_table = Table(
        title="Automation Analytics"
    )

    analytics_table.add_column("Metric")
    analytics_table.add_column("Value")

    for key, value in analytics.items():

        analytics_table.add_row(
            key.replace("_", " ").title(),
            str(value)
        )

    console.print(analytics_table)

def run():

    db = Database(
        settings.DATABASE_PATH
    )

    director = DirectorAgent()

    pricing_agent = PricingAgent()

    context_manager = ContextManager()

    history_manager = HistoryManager()

    client_manager = ClientManager()

    client_scoring = ClientScoring()

    service_recommendation = (
    ServiceRecommendationEngine()
    )

    crm_manager = (
    CRMManager()
    )
    
    sales_manager = (
    SalesManager()
    )

    scheduler_manager = (
    SchedulerManager()
    )

    automation_manager = (
        AutomationManager()
    )

    print_header()

    console.print(
        "[green]Database Connected[/green]"
    )

    console.print()

    while True:

        brief = console.input(
            "[bold cyan]Design Brief > [/bold cyan]"
        )

        if brief.lower() in [
            "exit",
            "quit"
        ]:
            break

        #
        # PHASE 2C
        #

                #
        # PHASE 2E
        #

        if CommandRouter.is_command(
            brief,
            "note client "
        ):

            parts = brief.split()

            if len(parts) < 4:

                console.print(
                    "[yellow]Format: note client <nama> <catatan>[/yellow]"
                )

                continue

            client_name = (
                parts[2]
                .upper()
            )

            note = " ".join(
                parts[3:]
            )

            client_manager.add_client_note(
                client_name,
                note
            )

            console.print(
                f"[green]Note saved for {client_name}[/green]"
            )

            continue
        
        if CommandRouter.is_command(
            brief,
            "show client "
        ):

            client_name = (
                brief
                .replace(
                    "show client ",
                    ""
                )
                .strip()
                .upper()
            )

            client = (
                client_manager.get_client(
                    client_name
                )
            )

            if client:

                projects = (
                    client_manager.get_client_projects(
                        client_name
                    )
                )

                intelligence = (
                    client_manager.get_client_intelligence(
                        client_name
                    )
                )

                notes = (
                    client_manager.get_client_notes(
                        client_name
                    )
                )

                show_client(
                    client,
                    projects,
                    intelligence,
                    notes
                )

            else:

                console.print(
                    "[yellow]Client tidak ditemukan[/yellow]"
                )

            continue

        if brief.lower() == "top clients":

            ranking = (
                client_scoring.get_client_ranking()
            )

            show_client_ranking(
                ranking
            )

            continue

        if CommandRouter.is_command(
            brief,
            "score client "
        ):

            client_name = (
                brief
                .replace(
                    "score client ",
                    ""
                )
                .strip()
                .upper()
            )

            try:

                score = (
                    client_scoring.calculate_score(
                        client_name
                    )
                )

                show_client_score(
                    score
                )

            except Exception as e:

                console.print(
                    f"[red]{str(e)}[/red]"
                )

            continue

        if CommandRouter.is_command(
            brief,
            "continue client "
        ):

            client_name = (
                brief
                .replace(
                    "continue client ",
                    ""
                )
                .strip()
                .upper()
            )

            project = (
                client_manager.get_client_last_project(
                    client_name
                )
            )

            if not project:

                console.print(
                    f"[red]No project found for {client_name}[/red]"
                )

                continue

            console.print()

            console.print(
                Panel.fit(
                    (
                        f"[bold]Client[/bold] : {client_name}\n\n"
                        f"[bold]Last Project[/bold]\n"
                        f"{project['brief']}\n\n"
                        f"[bold]Workflow[/bold]\n"
                        f"{project['workflow']}\n\n"
                        f"[bold]Recommended Next Steps[/bold]\n"
                        f"1. Brand Guideline\n"
                        f"2. Company Profile\n"
                        f"3. Social Media Kit"
                    ),
                    title="Project Continuation"
                )
            )

            continue

        if CommandRouter.is_command(
            brief,
            "recommend client "
        ):

            client_name = (
                brief
                .replace(
                    "recommend client ",
                    ""
                )
                .strip()
                .upper()
            )

            recommendation = (
                service_recommendation
                .recommend(
                    client_name
                )
            )

            if recommendation:

                show_service_recommendation(
                    recommendation
                )

            else:

                console.print(
                    "[yellow]Client tidak ditemukan[/yellow]"
                )

            continue

        if brief.lower() == (
            "crm dashboard"
        ):

            summary = (
                crm_manager
                .get_dashboard_summary()
            )

            show_crm_dashboard(
                summary
            )

            continue

        if CommandRouter.is_command(
            brief,
            "crm update "
        ):

            parts = (
                brief.split()
            )

            if len(parts) < 4:

                console.print(
                    "[yellow]Format:[/yellow]"
                )

                console.print(
                    "crm update CLIENT STATUS"
                )

                continue

            client_name = (
                parts[2]
                .upper()
            )

            status = (
                parts[3]
                .upper()
            )

            success = (
                crm_manager
                .update_pipeline(
                    client_name,
                    status
                )
            )

            if success:

                show_pipeline_update_result(
                    client_name,
                    status
                )

            else:

                console.print(
                    "[red]Invalid status[/red]"
                )

            continue

        if CommandRouter.is_command(
            brief,
            "crm client "
        ):

            client_name = (
                brief
                .replace(
                    "crm client ",
                    ""
                )
                .strip()
                .upper()
            )

            pipeline = (
                crm_manager
                .get_pipeline(
                    client_name
                )
            )

            show_crm_pipeline(
                pipeline
            )

            continue

        if brief.lower() == (
            "sales leaderboard"
        ):

            leaderboard = (
                sales_manager
                .get_leaderboard()
            )

            show_sales_leaderboard(
                leaderboard
            )

        
            continue

        if brief.lower() == (
            "sales pipeline"
        ):

            analytics = (
                sales_manager
                .get_pipeline_analytics()
            )

            show_pipeline_analytics(
                analytics
            )

            continue

        if brief.lower() == (
            "sales forecast"
        ):

            summary = (
                sales_manager
                .get_forecast_summary()
            )

            show_forecast_summary(
                summary
            )

            continue

        if brief.lower() == (
            "sales opportunities"
        ):

            opportunities = (
                sales_manager
                .get_opportunities()
            )

            show_opportunities(
                opportunities
            )

            continue       

        if CommandRouter.is_command(
            brief,
            "sales client "
        ):

            client_name = (
                brief
                .replace(
                    "sales client ",
                    ""
                )
                .strip()
                .upper()
            )

            strategy = (
                sales_manager
                .generate_strategy(
                    client_name
                )
            )

            show_sales_strategy(
                strategy
            )

            continue

        if brief.lower() == "schedule list":

            tasks = (
                scheduler_manager.list_tasks()
            )

            show_scheduler_tasks(
                tasks
            )

            continue

        if (
            brief.lower()
            ==
            "schedule dashboard"
        ):

            dashboard = (
                scheduler_manager
                .get_dashboard()
            )

            show_scheduler_dashboard(
                dashboard
            )

            continue

        if brief.lower().startswith(
            "schedule done "
        ):

            task_id = int(
                brief.replace(
                    "schedule done ",
                    ""
                )
            )

            scheduler_manager.complete_task(
                task_id
            )

            console.print(
                "[green]Task completed[/green]"
            )

            continue

        if brief.lower().startswith(
            "schedule add "
        ):

            parts = (
                brief.replace(
                    "schedule add ",
                    ""
                )
                .strip()
                .rsplit(
                    " ",
                    1
                )
            )
            print(parts)

            if len(parts) != 2:

                console.print(
                    "[red]Format:[/red] schedule add TITLE YYYY-MM-DD"
                )

                continue

            title = parts[0]

            date = parts[1]

            scheduler_manager.create_task(
                title,
                date
            )

            console.print(
                "[green]Task created[/green]"
            )

            continue

        if brief.lower() == "schedule analytics":

            analytics = (
                history_manager.get_analytics()
            )

            show_analytics(
                analytics
            )

            continue

        if brief.lower() == "schedule upcoming":

            tasks = scheduler_manager.get_upcoming_tasks()

            console.print(
                "\n[bold italic]Upcoming Tasks[/bold italic]"
            )

            table = Table()

            table.add_column("ID")
            table.add_column("Title")
            table.add_column("Date")

            for task in tasks:
                table.add_row(
                    str(task["id"]),
                    task["title"],
                    task["date"]
                )

            console.print(table)

            continue

        if brief.lower() == "schedule completed":

            tasks = scheduler_manager.get_completed_tasks()

            console.print(
                "\n[bold italic]Completed Tasks[/bold italic]"
            )

            table = Table()

            table.add_column("ID")
            table.add_column("Title")
            table.add_column("Date")

            for task in tasks:
                table.add_row(
                    str(task["id"]),
                    task["title"],
                    task["date"]
                )

            console.print(table)

            continue

        if brief.lower() == "automation run":

            executed = (
                automation_manager.run_rules()
            )

            console.print(
                f"\n[bold green]{executed} automation rule executed[/bold green]"
            )

            continue

        if brief.lower() == "automation dashboard":

            dashboard = (
                automation_manager.automation_dashboard()
            )

            show_automation_dashboard(
                dashboard
            )

            continue


        if brief.lower() == "automation analytics":

            analytics = (
                automation_manager.automation_analytics()
            )

            show_automation_analytics(
                analytics
            )

            continue

        if brief.lower() == "automation report":

            report = (
                automation_manager.automation_report()
            )

            show_automation_report(
                report
            )

            continue

        if brief.lower().startswith(
            "lanjutkan"
        ):

            project = (
                 history_manager.find_project(
                     brief
                )
            )

            console.print()

            if project:

                console.print(
                    "[green]Project Found[/green]"
                )

                console.print(
                    f"Brief : {project[0]}"
                )

                console.print(
                    f"Workflow : {project[1]}"
                )

                console.print(
                    f"Project Type : {project[2]}"
                )

                console.print(
                    f"Category : {project[6]}"
                )

                console.print(
                    f"Tags : {project[7]}"
                )

            else:

                console.print(
                    "[yellow]Project tidak ditemukan[/yellow]"
                )

                console.print()

            continue

        detected_client = (
            client_manager
            .save_client_if_needed(
                brief
                )
        )

        if detected_client:

            console.print(
                f"[cyan]Client Saved:[/cyan] {detected_client}"
            )

        result = director.analyze_brief(
            brief
        )

        context = ProjectContext(
            project_type=result.project_type,
            client_goal=result.client_goal,
            target_audience=result.target_audience,
            creative_direction=result.creative_direction,
            workflow=result.workflow
        )

        context_manager.save_project_context(
            context
        )

        history_manager.save_project(
            brief,
            result
        )

        loaded_context = (
            context_manager.load_project_context()
        )

        console.print(
            "\n[green]Context Loaded[/green]"
        )

        console.print(
            loaded_context
        )

        console.print()

        console.print(
            Panel(
                result.workflow,
                title="Workflow",
                border_style="green"
            )
        )

        console.print_json(
            data=result.model_dump()
        )

        pricing = pricing_agent.generate_price(
            project_type=result.project_type,
            client_goal=result.client_goal,
            target_audience=result.target_audience
        )

        console.print()

        show_pricing(
            pricing
        )

        console.print()

    db.close()


if __name__ == "__main__":
    run()