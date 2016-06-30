from tuning.player import PlayerTuning

# Function to reset character's stats to base values,
#   and restore infusion points as appropriate
def resetStats(entityTuning, entity, current):
    component = entity.stats

    # Get base character stats to build on
    baseStatsAtLevel = PlayerTuning.STATS

    # Iterate through all levels until current
    for level in xrange(1, current):
        stats = None

        # Get (current) correct level bracket
        for levelStats in monsterTuning.LEVEL_STATS:
            if levelStats.level > level:
                break
            stats = levelStats
        
        # Add the stats to our base stats
        for statName, value in stats.iteritems():
            if statName == 'level':
                continue
            curStatVal = getattr(baseStatsAtLevel, statName)
            setattr(baseStatsAtLevel, statName, curStatVal + value)

    # Assign character all 'infusion points'
    # Calculate the 'long' way to account for points obtained from
    #   other sources - source code seems to imply leveling up
    #   is not the only way to get stat points
    infusionPoints = 0 # (current-1) * PlayerTuning.INFUSIONS_GAINED_PER_LEVEL

    # Set the character's stats to what their base values would be
    component = entity.stats
    for statName, baseValue in baseStatsAtLevel:
        stat = component.get(statName)
        infusionPoints += (stat - baseValue)
        stat.set(baseValue)

    component.grantInfusions(infusionPoints)
