# engine.py
from typing import Dict, List, Optional

class PromptEngine:
    def __init__(self, styles: Dict, lighting: Dict, materials: List):
        self.styles = styles
        self.lighting = lighting
        self.materials = materials

    def construct_prompt(
        self,
        core_subject: str,
        style_key: str,
        lighting_key: str,
        selected_materials: Optional[List[str]] = None,
        intensity: float = 1.0
    ) -> str:
        """Assembles the final creative asset prompt string."""
        style_desc = self.styles.get(style_key, "")
        lighting_desc = self.lighting.get(lighting_key, "")
        
        material_str = ", ".join(selected_materials) if selected_materials else self.materials[0]
        
        # Constructing the structural syntax
        prompt_segments = [
            f"Masterpiece asset of {core_subject}",
            f"rendered in {style_key} aesthetic ({style_desc})",
            f"composed of {material_str}",
            f"illuminated by {lighting_desc}",
            f"dark machine surrealism, highly detailed, photorealistic, cinematic composition"
        ]
        
        # Join segments cleanly using standard punctuation
        final_prompt = ", ".join([seg for seg in prompt_segments if seg])
        
        if intensity > 1.0:
            final_prompt += ", hyper extreme detailing, emphasized structural complexity"
            
        return final_prompt
