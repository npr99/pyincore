"""pyincore.analyses.epfdamage.epfutil

Copyright (c) 2017 University of Illinois and others.  All rights reserved.
This program and the accompanying materials are made available under the
terms of the BSD-3-Clause which accompanies this distribution,
and is available at https://opensource.org/licenses/BSD-3-Clause

"""


class EpfUtil:
    """Utility methods for the electric power facility damage analysis."""
    EPF_HAZUS_FRAGILITY_KEYS = {
        "ESS1", "Low Voltage (115 KV) Substation (Anchored/Seismic Components)",
        "ESS2", "Low Voltage (115 KV) Substation (Unanchored/Standard Components)",
        "ESS3", "Medium Voltage (230 KV) Substation (Anchored/Seismic Components)",
        "ESS4", "Medium Voltage (230 KV) Substation (Unanchored/Standard Components)",
        "ESS5", "High Voltage (500 KV) Substation (Anchored/Seismic Components)",
        "ESS6", "High Voltage (500 KV) Substation (Unanchored/Standard Components)",
        "EPP1", "Small Generation Facility (Anchored Components)",
        "EPP2", "Small Generation Facility (Unanchored Components)",
        "EPP3", "Medium/Large Generation Facility (Anchored Components)",
        "EPP4", "Medium/Large Generation Facility (Unanchored Components)",
        "EDC1", "Distribution Circuit (Seismic Components)",
        "EDC2", "Distribution Circuit (Standard Components)"
    }

    DEFAULT_FRAGILITY_KEY = "Non-Retrofit Fragility ID Code"

    @staticmethod
    def get_hazard_demand_type(fragility_set, hazard_type):
        """Run analysis for single epf (facility).

        Args:
            fragility_set (obj): Fragility set applied to the facility.
            hazard_type (obj): A single epf from input inventory set.

        Returns:
            obj: A string with hazard demand_type.

        """
        fragility_hazard_type = fragility_set['demandType'].lower()
        hazard_demand_type = fragility_hazard_type

        if hazard_type.lower() == "earthquake":
            hazard_demand_type = fragility_hazard_type

        return hazard_demand_type
