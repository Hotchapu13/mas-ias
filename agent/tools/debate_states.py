from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from datetime import datetime

@dataclass
class Task:
    """Represents an academic or personal task."""
    id: str
    title: str
    weight: float  # Percentage of final grade (0.0 to 1.0)
    deadline: datetime
    estimated_hours: float
    priority_score: Optional[float] = 0.0
    status: str = "pending"  # pending, in_progress, completed

@dataclass
class AgentProposal:
    """Holds the specific output and rationale from a single agent."""
    agent_name: str  # Scheduler, Welfare, or Academic
    proposed_schedule: List[Dict[str, Any]]  # List of time slots and task IDs
    rationale: str  # The reasoning behind this specific plan
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass
class Critique:
    """Represents one agent's feedback on another agent's proposal."""
    from_agent: str
    target_agent: str
    critique_text: str
    points_of_conflict: List[str]

@dataclass
class DebateState:
    """
    The central state for the MAS-IAS Free-MAD protocol.
    This object is passed between agents and updated as the debate progresses.
    """
    # 1. User Inputs
    user_profile: Dict[str, Any] = field(default_factory=lambda: {
        "name": "",
        "major": "",
        "sleep_preference": "8h",
        "current_stress_level": 5,  # 1-10
        "fixed_commitments": []     # Lectures, work, etc.
    })
    
    # 2. Domain Data
    task_list: List[Task] = field(default_factory=list)
    
    # 3. Parallel Debate Data
    # Keys: 'Scheduler', 'Welfare', 'Academic'
    proposals: Dict[str, AgentProposal] = field(default_factory=dict)
    
    # 4. Cross-Critique Data
    critiques: List[Critique] = field(default_factory=list)
    
    # 5. The Judge's Decision
    final_selection: Optional[str] = None  # Name of the winning agent
    judge_rationale: Optional[str] = None
    scoring_breakdown: Dict[str, Dict[str, float]] = field(default_factory=dict)
    
    # 6. Global History
    debate_transcript: List[Dict[str, str]] = field(default_factory=list)

    def add_to_transcript(self, role: str, message: str):
        """Helper to log the flow of the debate."""
        self.debate_transcript.append({
            "timestamp": datetime.now().isoformat(),
            "role": role,
            "content": message
        })

    def get_full_context_for_judge(self) -> str:
        """Serializes the state for the Scoring Agent's review."""
        # This helper is vital for feeding the LLM the full debate history
        return f"Proposals: {self.proposals}\nCritiques: {self.critiques}"