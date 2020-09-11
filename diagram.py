# diagram.py
from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.onprem.ci import Jenkins, Circleci
from diagrams.onprem.container import Docker
from diagrams.onprem.vcs import Git, Github, Gitlab
from diagrams.azure import devops
from diagrams.generic.storage import Storage
from diagrams.alibabacloud.application import RdCloud

with Diagram("Upskilling Malmö", show=True, direction="TB"):
    # Timeline
    now = Storage("Now")

    ## -------------------------------------------------------
    ## PAST
    ## -------------------------------------------------------
    # Castle: Git
    with Cluster("Git"):
        git = Git("")
    git >> now

    ## -------------------------------------------------------
    ## FUTURE
    ## -------------------------------------------------------
    # Castle: Docker
    with Cluster("Docker"):
        docker = Docker("")
    now >> docker

    # Castle: Build Tools
    with Cluster("Build Tools Familiarity"):
        buildtools = ELB("")
        jenkins = Jenkins("Jenkins")
        buildtools << Edge(color="brown", style="dashed") << [
            jenkins,
            Gitlab("Gitlab runners"),
            Github("Github actions"),
            Circleci("Circle CI"),
            devops.Pipelines("Azure pipelines"),
            ]
    now >> buildtools

    # Castle: JCasC
    with Cluster("Jenkins (w/ JCasc)"):
        jenkinsjcasc = Jenkins("Jenkins (w/ JCasc)")
        trainingmaterial = EC2("Training material")
        jenkinsjcasc << Edge(color="brown", style="dashed") << [
            trainingmaterial,
            ]
    docker >> jenkinsjcasc
    jenkins >> jenkinsjcasc
    jenkinsjcasc

    # Castle: Basic knowledge on modern ops tooling
    with Cluster("Modern ops tooling"):
        opstooling = RdCloud("")
    now >> opstooling

    # Castle: Workshop facilitation
    with Cluster("Workshop facilitation"):
        workshop = ELB("")
    now >> workshop

    # Castle: Value Stream Mapping
    with Cluster("Value Stream Mapping"):
        valuestreammapping = ELB("")
    workshop >> valuestreammapping

    # Castle: Coach TDD Mob programming
    with Cluster("Coach TDD Mob programming"):
        tddmobprogramming = ELB("")
        tdd = EC2("Coach TDD")
        mobprogramming = EC2("Mob programming")
        tddmobprogramming << Edge(color="brown", style="dashed") << [
            tdd,
            mobprogramming,
            ]
    now >> tddmobprogramming
