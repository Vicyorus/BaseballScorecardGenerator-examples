import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ MIN, 2018-06-20
# https://www.baseball-reference.com/boxes/MIN/MIN201806200.shtml
# https://www.mlb.com/gameday/red-sox-vs-twins/2018/06/20/530506/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-20 20:11-23:24",
        "at": "Target Field, Minneapolis, MN",
        "att": "33,153",
        "temp": "77F, Partly Cloudy",
        "wind": "11mph, In From CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                11: "Rafael Devers",
                12: "Brock Holt",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                24: "David Price",
                # Bench
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                37: "Heath Hembree",
                63: "Robby Scott",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [24, 57, 41, 61, 63],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [2, "6"],
                [28, "0"],
                [18, "3"],
                [11, "5"],
                [12, "4"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [36, "SS"],
                [23, "C"],
                [3, "C"],
            ],
            "bullpen": [57, 35, 44, 22, 41, 61, 37, 63, 46, 76, 56, 32],
        },
        "home": {
            "team": "Minnesota Twins",
            "starter": 31,
            "roster": {
                # Lineup
                36: "Robbie Grossman",
                20: "Eddie Rosario",
                5: "Eduardo Escobar",
                2: "Brian Dozier",
                99: "Logan Morrison",
                16: "Ehire Adrianza",
                26: "Max Kepler",
                23: "Mitch Garver",
                24: "Ryan LaMarre",
                # Starting pitcher
                31: "Lance Lynn",
                # Bench
                7: "Joe Mauer",
                45: "Taylor Motter",
                46: "Bobby Wilson",
                # Bullpen
                77: "Fernando Romero",
                38: "Matt Belisle",
                43: "Addison Reed",
                68: "Matt Magill",
                39: "Trevor Hildenberger",
                12: "Jake Odorizzi",
                17: "José Berríos",
                56: "Fernando Rodney",
                57: "Ryan Pressly",
                55: "Taylor Rogers",
                32: "Zach Duke",
                44: "Kyle Gibson",
            },
            "lefties": [55, 32],
            "lineup": [
                [36, "0"],
                [20, "7"],
                [5, "5"],
                [2, "4"],
                [99, "3"],
                [16, "6"],
                [26, "9"],
                [23, "2"],
                [24, "8"],
            ],
            "bench": [
                [7, "C"],
                [45, "2B"],
                [46, "C"],
            ],
            "bullpen": [77, 38, 43, 68, 39, 12, 17, 56, 57, 55, 32, 44],
        },
        "umpires": {
            "HP": "Jeff Nelson",
            "1B": "Tom Woodring",
            "2B": "Scott Barry",
            "3B": "Carlos Torres",
        },
    },
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: MIN #31 Lance Lynn
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("F9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b c")
t1.out("G6-3")

# 3. BOS #2  Xander Bogaerts (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.hit(2)

# 4. BOS #28 J.D. Martinez (X - 2 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b c s f b s")
t1.out("K")


# Bot 1st
# Pitching: BOS #24 David Price
b1 = game.new_inning()

# 1. MIN #36 Robbie Grossman (X - X - X)
b1.new_ab()
b1.pitch_list("c c b b")
b1.hit(4)

# 2. MIN #20 Eddie Rosario (X - X - X)
b1.new_ab()
b1.hit(1)
b1.thrown_out(2, "2 POCS", 2, 24)

# 3. MIN #5  Eduardo Escobar (X - X - 20)
b1.new_ab()
b1.pitch_list("f c")
b1.out("F9")

# 4. MIN #2  Brian Dozier (X - X - 20)
b1.new_ab()
b1.pitch_list("b b s b 1 c c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: MIN #31 Lance Lynn
t2 = game.new_inning()

# 5. BOS #18 Mitch Moreland (X - X - X)
t2.new_ab()
t2.pitch_list("c f b b b f b")
t2.reach("BB")
t2.advance(2, "12 BB")
t2.advance("U", "19 E3")

# 6. BOS #11 Rafael Devers (X - X - 18)
t2.new_ab()
t2.pitch_list("s")
t2.out("(F)P3")

# 7. BOS #12 Brock Holt (X - X - 18)
t2.new_ab()
t2.pitch_list("b b b c b")
t2.reach("BB")
t2.advance(3, "19 E3")
t2.thrown_out(4, "50 POCS", 3, 31)

# 8. BOS #7  Christian Vázquez (X - 18 - 12)
t2.new_ab(is_risp=True)
t2.pitch_list("b c")
t2.out("L3")

# 9. BOS #19 Jackie Bradley Jr. (X - 18 - 12)
t2.new_ab(is_risp=True)
t2.pitch_list("c b d f")
t2.error(3)
t2.reach("E3")

# 1. BOS #50 Mookie Betts (12 - X - 19)
t2.new_ab(is_risp=True)
t2.pitch_list("c b b s f f b 3")
t2.no_ab("POCS")


# Bot 2nd
# Pitching: BOS #24 David Price
b2 = game.new_inning()

# 5. MIN #99 Logan Morrison (X - X - X)
b2.new_ab()
b2.pitch_list("b b s b")
b2.out("F9")

# 6. MIN #16 Ehire Adrianza (X - X - X)
b2.new_ab()
b2.pitch_list("c b f b")
b2.hit(1)

# 7. MIN #26 Max Kepler (X - X - 16)
b2.new_ab()
b2.pitch_list("d")
b2.out("L6")

# 8. MIN #23 Mitch Garver (X - X - 16)
b2.new_ab()
b2.pitch_list("c")
b2.out("L4")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: MIN #31 Lance Lynn
t3 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("b s b")
t3.hit(1)
t3.advance(2, "16 G5-3")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t3.new_ab()
t3.pitch_list("b")
t3.out("G5-3")

# 3. BOS #2  Xander Bogaerts (X - 50 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c b b b f")
t3.out("G5-3")

# 4. BOS #28 J.D. Martinez (X - 50 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("f b b b s f")
t3.out("G6-3")


# Bot 3rd
# Pitching: BOS #24 David Price
b3 = game.new_inning()

# 9. MIN #24 Ryan LaMarre (X - X - X)
b3.new_ab()
b3.pitch_list("c b s b b")
b3.out("F9")

# 1. MIN #36 Robbie Grossman (X - X - X)
b3.new_ab()
b3.out("F7")

# 2. MIN #20 Eddie Rosario (X - X - X)
b3.new_ab()
b3.pitch_list("b b s c")
b3.hit(3)

# 3. MIN #5  Eduardo Escobar (20 - X - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b")
b3.out("G1-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: MIN #31 Lance Lynn
t4 = game.new_inning()

# 5. BOS #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.pitch_list("b f")
t4.hit(1)
t4.advance(2, "11 BB")
t4.advance(3, "12 DP4-6-3")

# 6. BOS #11 Rafael Devers (X - X - 18)
t4.new_ab()
t4.pitch_list("b b b b")
t4.reach("BB")
t4.thrown_out(2, "12 DP4-6-3", 1, 31)

# 7. BOS #12 Brock Holt (X - 18 - 11)
t4.new_ab(is_risp=True)
t4.pitch_list("b")
t4.out("DP4-6-3")

# 8. BOS #7  Christian Vázquez (18 - X - X)
t4.new_ab(is_risp=True)
t4.pitch_list("f b s s")
t4.out("K")


# Bot 4th
# Pitching: BOS #24 David Price
b4 = game.new_inning()

# 4. MIN #2  Brian Dozier (X - X - X)
b4.new_ab()
b4.pitch_list("c b b s b")
b4.hit(2)
b4.advance(3, "16 DP5-4-3")
b4.advance(4, "26 HR")

# 5. MIN #99 Logan Morrison (X - 2 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b c b s b b")
b4.reach("BB")
b4.thrown_out(2, "16 DP5-4-3", 1, 24)

# 6. MIN #16 Ehire Adrianza (X - 2 - 99)
b4.new_ab(is_risp=True)
b4.pitch_list("s")
b4.out("DP5-4-3")

# 7. MIN #26 Max Kepler (2 - X - X)
b4.new_ab(is_risp=True)
b4.pitch_list("f b f")
b4.hit(4, rbis=2)

# 8. MIN #23 Mitch Garver (X - X - X)
b4.new_ab()
b4.pitch_list("b b")
b4.out("F9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: MIN #31 Lance Lynn
t5 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("b f b b b")
t5.reach("BB")
t5.advance(2, "50 G4-3")
t5.advance(3, "2 FC5-4")

# 1. BOS #50 Mookie Betts (X - X - 19)
t5.new_ab()
t5.out("G4-3")

# 2. BOS #16 Andrew Benintendi (X - 19 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("s c b b b b")
t5.reach("BB")
t5.thrown_out(2, "2 FC5-4", 2, 31)

# 3. BOS #2  Xander Bogaerts (X - 19 - 16)
t5.new_ab(is_risp=True)
t5.pitch_list("c s b b f")
t5.reach("FC5-4")

# 4. BOS #28 J.D. Martinez (19 - X - 2)
t5.new_ab(is_risp=True)
t5.pitch_list("b b f")
t5.out("G4-3")


# Bot 5th
# Pitching: BOS #24 David Price
b5 = game.new_inning()

# 9. MIN #24 Ryan LaMarre (X - X - X)
b5.new_ab()
b5.pitch_list("b f f b")
b5.hit(1)
b5.error(5)
b5.advance(2, "5 E5")

# 1. MIN #36 Robbie Grossman (X - X - 24)
b5.new_ab()
b5.pitch_list("l b")
b5.out("F8")

# 2. MIN #20 Eddie Rosario (X - X - 24)
b5.new_ab()
b5.pitch_list("b f f s 1")
b5.out("K")

# 3. MIN #5  Eduardo Escobar (X - X - 24)
b5.new_ab()
b5.pitch_list("b b s s f f")
b5.reach("FC5")

# 4. MIN #2  Brian Dozier (X - 24 - 5)
b5.new_ab(is_risp=True)
b5.pitch_list("b c f")
b5.out("L8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: MIN #55 Taylor Rogers
t6 = game.new_inning()

# Pitching change (MIN): #55 Taylor Rogers replaces #31 Lance Lynn
t6.pitching_substitution(55)

# 5. BOS #18 Mitch Moreland (X - X - X)
t6.new_ab()
t6.pitch_list("c b b c f s")
t6.out("K")

# 6. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("b c")
t6.out("F9")

# 7. BOS #12 Brock Holt (X - X - X)
t6.new_ab()
t6.pitch_list("c b b b c c")
t6.out("!K")


# Bot 6th
# Pitching: BOS #24 David Price
b6 = game.new_inning()

# 5. MIN #99 Logan Morrison (X - X - X)
b6.new_ab()
b6.pitch_list("f f b b b")
b6.out("G3")

# 6. MIN #16 Ehire Adrianza (X - X - X)
b6.new_ab()
b6.pitch_list("c b f s")
b6.out("K")

# 7. MIN #26 Max Kepler (X - X - X)
b6.new_ab()
b6.pitch_list("b b")
b6.out("L4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: MIN #43 Addison Reed
t7 = game.new_inning()

# Pitching change (MIN): #43 Addison Reed replaces #55 Taylor Rogers
t7.pitching_substitution(43)

# 8. BOS #7  Christian Vázquez (X - X - X)
t7.new_ab()
t7.pitch_list("b f f b f b")
t7.out("G6-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.out("F8")

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.pitch_list("c s f f b")
t7.hit(1)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t7.new_ab()
t7.out("F9")


# Bot 7th
# Pitching: BOS #37 Heath Hembree
b7 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #24 David Price
b7.pitching_substitution(37)

# 8. MIN #23 Mitch Garver (X - X - X)
b7.new_ab()
b7.pitch_list("s")
b7.out("F8")

# 9. MIN #24 Ryan LaMarre (X - X - X)
b7.new_ab()
b7.pitch_list("b s c b c")
b7.out("!K")

# 1. MIN #36 Robbie Grossman (X - X - X)
b7.new_ab()
b7.pitch_list("c f")
b7.out("F9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: MIN #39 Trevor Hildenberger
t8 = game.new_inning()

# Pitching change (MIN): #39 Trevor Hildenberger replaces #43 Addison Reed
t8.pitching_substitution(39)

# 3. BOS #2  Xander Bogaerts (X - X - X)
t8.new_ab()
t8.pitch_list("b c c f f")
t8.out("G4-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t8.new_ab()
t8.pitch_list("b b c")
t8.out("L9")

# 5. BOS #18 Mitch Moreland (X - X - X)
t8.new_ab()
t8.pitch_list("b f s b f f s")
t8.out("K")


# Bot 8th
# Pitching: BOS #61 Brian Johnson
b8 = game.new_inning()

# Pitching change (BOS): #61 Brian Johnson replaces #37 Heath Hembree
b8.pitching_substitution(61)

# 2. MIN #20 Eddie Rosario (X - X - X)
b8.new_ab()
b8.pitch_list("b b b b")
b8.reach("BB")
b8.advance(4, "2 2B")

# 3. MIN #5  Eduardo Escobar (X - X - 20)
b8.new_ab()
b8.pitch_list("c f b f s")
b8.out("K")

# 4. MIN #2  Brian Dozier (X - X - 20)
b8.new_ab()
b8.pitch_list("c b 1 1 d b c 1")
b8.hit(2, rbis=1)
b8.advance(3, "99 SB")

# 5. MIN #99 Logan Morrison (X - 2 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("d c c b n b f f f f")
b8.out("G3")

# 6. MIN #16 Ehire Adrianza (2 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("f b c f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: MIN #56 Fernando Rodney
t9 = game.new_inning()

# Pitching change (MIN): #56 Fernando Rodney replaces #39 Trevor Hildenberger
t9.pitching_substitution(56)

# 6. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("F8")

# 7. BOS #12 Brock Holt (X - X - X)
t9.new_ab()
t9.pitch_list("c s b b b")
t9.out("G3-1")

# 8. BOS #7  Christian Vázquez (X - X - X)
t9.new_ab()
t9.pitch_list("b c")
t9.out("G5-3")

# Winning team: MIN
# WP: MIN #31 Lance Lynn
game.winning_pitcher(31)
# SV: MIN #56 Fernando Rodney
game.save_pitcher(56)

# Loser team: BOS
# LP: BOS #24 David Price
game.losing_pitcher(24, is_away_team=True)

# print(game)
game.generate_scorecard()
