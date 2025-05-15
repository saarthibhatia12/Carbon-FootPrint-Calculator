import os
import random

def get_suggestions(input_data, prediction):
    """
    Generate carbon footprint reduction suggestions based on user input without requiring API access.
    """
    # Dictionary of suggestions based on different lifestyle factors
    suggestion_templates = {
        "diet": {
            "omnivore": "Consider adopting a plant-based diet for at least 1-2 days per week to reduce your carbon footprint from food consumption.",
            "pescatarian": "Try reducing seafood consumption and incorporate more plant-based meals to further decrease your carbon footprint.",
            "vegetarian": "Consider transitioning to a fully vegan diet for some meals to further reduce your carbon footprint.",
            "vegan": "Continue your vegan diet and consider buying more local, seasonal produce to reduce transportation emissions."
        },
        "transport": {
            "private": "Consider carpooling, using public transport, or switching to a hybrid/electric vehicle to reduce emissions.",
            "public": "Great job using public transport! Consider walking or cycling for shorter journeys when possible.",
            "walk/bicycle": "Excellent choice using non-motorized transport! Continue this practice and encourage others to do the same."
        },
        "air_travel": {
            "never": "Keep avoiding air travel when possible, as it's one of the most carbon-intensive forms of transportation.",
            "rarely": "Consider offsetting your flight emissions through verified carbon offset programs.",
            "frequently": "Try to consolidate trips and choose direct flights to minimize your carbon footprint from air travel.",
            "very frequently": "Consider replacing some flights with video conferencing or alternative transport methods like trains for shorter distances."
        },
        "waste": {
            "high": "Start composting organic waste and increase recycling efforts to reduce landfill contributions.",
            "medium": "Aim for zero-waste by using reusable containers, buying in bulk, and avoiding single-use items.",
            "low": "Great job managing your waste! Continue minimizing packaging and consider a full zero-waste lifestyle."
        },
        "energy": {
            "coal": "Consider switching to renewable energy sources or a cleaner energy provider.",
            "electricity": "Install energy-efficient appliances and consider solar panels if feasible for your location.",
            "natural gas": "Improve home insulation and use a programmable thermostat to reduce heating needs.",
            "wood": "Ensure wood is sourced sustainably and consider supplementing with other renewable energy sources."
        },
        "general": [
            "Use energy-efficient LED bulbs throughout your home to reduce electricity consumption.",
            "Install a water-saving showerhead and take shorter showers to reduce water heating energy.",
            "Reduce food waste by planning meals carefully and composting organic waste.",
            "Buy second-hand clothing and goods when possible to reduce manufacturing emissions.",
            "Turn off and unplug electronic devices when not in use to avoid phantom energy consumption.",
            "Plant trees or support reforestation projects to offset your carbon emissions.",
            "Wash clothes in cold water and line-dry them instead of using a dryer.",
            "Support businesses that prioritize sustainability and have eco-friendly practices."
        ]
    }
    
    try:
        # Determine waste level based on bag size and count
        waste_level = "low"
        if input_data["Waste Bag Size"] in ["medium", "large"] and input_data["Waste Bag Weekly Count"] > 3:
            waste_level = "medium"
        elif input_data["Waste Bag Size"] in ["large", "extra large"] and input_data["Waste Bag Weekly Count"] > 5:
            waste_level = "high"
        
        # Collect relevant suggestions
        suggestions = []
        
        # Add diet suggestion
        diet = input_data["Diet"]
        if diet in suggestion_templates["diet"]:
            suggestions.append(suggestion_templates["diet"][diet])
        
        # Add transport suggestion
        transport = input_data["Transport"]
        if transport in suggestion_templates["transport"]:
            suggestions.append(suggestion_templates["transport"][transport])
        
        # Add air travel suggestion
        air_travel = input_data["Frequency of Traveling by Air"]
        if air_travel in suggestion_templates["air_travel"]:
            suggestions.append(suggestion_templates["air_travel"][air_travel])
        
        # Add waste suggestion
        suggestions.append(suggestion_templates["waste"][waste_level])
        
        # Add energy suggestion
        energy = input_data["Heating Energy Source"]
        if energy in suggestion_templates["energy"]:
            suggestions.append(suggestion_templates["energy"][energy])
        
        # Add general suggestions if needed to reach 5
        general = suggestion_templates["general"].copy()
        random.shuffle(general)
        
        while len(suggestions) < 5:
            if general:
                suggestions.append(general.pop(0))
            else:
                break
        
        return {"suggestions": suggestions[:5]}
        
    except Exception as e:
        return {"error": f"Error generating suggestions: {str(e)}"}
