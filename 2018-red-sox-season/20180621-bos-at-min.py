import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ MIN, 2018-06-21
# https://www.baseball-reference.com/boxes/MIN/MIN201806210.shtml
# https://www.mlb.com/gameday/red-sox-vs-twins/2018/06/21/530520/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-21 13:10-16:08",
        "at": "Target Field, Minneapolis, MN",
        "att": "32,631",
        "temp": "72F, Partly Cloudy",
        "wind": "10mph, In From CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                12: "Brock Holt",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                41: "Chris Sale",
                61: "Brian Johnson",
                37: "Heath Hembree",
                63: "Robby Scott",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 61, 63, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [18, "3"],
                [2, "6"],
                [11, "5"],
                [12, "4"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [36, "SS"],
                [23, "C"],
                [7, "C"],
            ],
            "bullpen": [57, 35, 44, 41, 61, 37, 63, 24, 46, 76, 56, 32],
        },
        "home": {
            "team": "Minnesota Twins",
            "starter": 44,
            "roster": {
                # Lineup
                7: "Joe Mauer",
                2: "Brian Dozier",
                5: "Eduardo Escobar",
                99: "Logan Morrison",
                36: "Robbie Grossman",
                26: "Max Kepler",
                16: "Ehire Adrianza",
                24: "Ryan LaMarre",
                46: "Bobby Wilson",
                # Starting pitcher
                44: "Kyle Gibson",
                # Bench
                45: "Taylor Motter",
                20: "Eddie Rosario",
                23: "Mitch Garver",
                # Bullpen
                77: "Fernando Romero",
                38: "Matt Belisle",
                43: "Addison Reed",
                31: "Lance Lynn",
                68: "Matt Magill",
                39: "Trevor Hildenberger",
                12: "Jake Odorizzi",
                17: "José Berríos",
                56: "Fernando Rodney",
                57: "Ryan Pressly",
                55: "Taylor Rogers",
                32: "Zach Duke",
            },
            "lefties": [55, 32],
            "lineup": [
                [7, "3"],
                [2, "4"],
                [5, "5"],
                [99, "0"],
                [36, "7"],
                [26, "9"],
                [16, "6"],
                [24, "8"],
                [46, "2"],
            ],
            "bench": [
                [45, "2B"],
                [20, "LF"],
                [23, "DH"],
            ],
            "bullpen": [77, 38, 43, 31, 68, 39, 12, 17, 56, 57, 55, 32],
        },
        "umpires": {
            "HP": "Tom Woodring",
            "1B": "Scott Barry",
            "2B": "Carlos Torres",
            "3B": "Jeff Nelson",
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
# Pitching: MIN #44 Kyle Gibson
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b f b")
t1.hit(1)
t1.advance(2, "28 BB")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t1.new_ab()
t1.pitch_list("b")
t1.out("L7")

# 3. BOS #28 J.D. Martinez (X - X - 50)
t1.new_ab()
t1.pitch_list("1 b b b b")
t1.reach("BB")

# 4. BOS #18 Mitch Moreland (X - 50 - 28)
t1.new_ab(is_risp=True)
t1.pitch_list("s b f f f b b c")
t1.out("!K")

# 5. BOS #2  Xander Bogaerts (X - 50 - 28)
t1.new_ab(is_risp=True)
t1.pitch_list("d b c f f")
t1.out("L8")


# Bot 1st
# Pitching: BOS #22 Rick Porcello
b1 = game.new_inning()

# 1. MIN #7  Joe Mauer (X - X - X)
b1.new_ab()
b1.pitch_list("c f b")
b1.out("G4-3")

# 2. MIN #2  Brian Dozier (X - X - X)
b1.new_ab()
b1.pitch_list("c b b t")
b1.out("G5-3")

# 3. MIN #5  Eduardo Escobar (X - X - X)
b1.new_ab()
b1.reach("HBP")
b1.advance(2, "99 1B")

# 4. MIN #99 Logan Morrison (X - X - 5)
b1.new_ab()
b1.pitch_list("c")
b1.hit(1)

# 5. MIN #36 Robbie Grossman (X - 5 - 99)
b1.new_ab(is_risp=True)
b1.pitch_list("f f f")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: MIN #44 Kyle Gibson
t2 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("s t c")
t2.out("!K")

# 7. BOS #12 Brock Holt (X - X - X)
t2.new_ab()
t2.out("G3")

# 8. BOS #3  Sandy León (X - X - X)
t2.new_ab()
t2.pitch_list("c f f b b b f b")
t2.reach("BB")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 3)
t2.new_ab()
t2.pitch_list("c b f b")
t2.out("L4")


# Bot 2nd
# Pitching: BOS #22 Rick Porcello
b2 = game.new_inning()

# 6. MIN #26 Max Kepler (X - X - X)
b2.new_ab()
b2.pitch_list("f b b b c")
b2.out("F8")

# 7. MIN #16 Ehire Adrianza (X - X - X)
b2.new_ab()
b2.pitch_list("f b b s b f f f s")
b2.out("K")

# 8. MIN #24 Ryan LaMarre (X - X - X)
b2.new_ab()
b2.pitch_list("c b b b b")
b2.reach("BB")

# 9. MIN #46 Bobby Wilson (X - X - 24)
b2.new_ab()
b2.out("F8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: MIN #44 Kyle Gibson
t3 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.out("P6")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("s s s")
t3.out("K")

# 3. BOS #28 J.D. Martinez (X - X - X)
t3.new_ab()
t3.pitch_list("b s s b c")
t3.out("!K")


# Bot 3rd
# Pitching: BOS #22 Rick Porcello
b3 = game.new_inning()

# 1. MIN #7  Joe Mauer (X - X - X)
b3.new_ab()
b3.pitch_list("f b f")
b3.out("G6-3")

# 2. MIN #2  Brian Dozier (X - X - X)
b3.new_ab()
b3.pitch_list("c s b b")
b3.out("L7")

# 3. MIN #5  Eduardo Escobar (X - X - X)
b3.new_ab()
b3.pitch_list("b f s f t")
b3.out("KT")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: MIN #44 Kyle Gibson
t4 = game.new_inning()

# Defensive change (MIN): #45 Taylor Motter replaces #5 Eduardo Escobar (3B), playing 3B, batting 3rd
t4.defensive_substitution(3, 45, "5")

# 4. BOS #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.pitch_list("c s b b b b")
t4.reach("BB")
t4.advance(2, "12 1B")
t4.advance(4, "3 1B")

# 5. BOS #2  Xander Bogaerts (X - X - 18)
t4.new_ab()
t4.pitch_list("f b f")
t4.out("L8")

# 6. BOS #11 Rafael Devers (X - X - 18)
t4.new_ab()
t4.pitch_list("f f s")
t4.out("K")

# 7. BOS #12 Brock Holt (X - X - 18)
t4.new_ab()
t4.pitch_list("b c")
t4.hit(1)
t4.advance(3, "3 1B")

# 8. BOS #3  Sandy León (X - 18 - 12)
t4.new_ab(is_risp=True)
t4.hit(1, rbis=1)

# 9. BOS #19 Jackie Bradley Jr. (12 - X - 3)
t4.new_ab(is_risp=True)
t4.pitch_list("c b")
t4.out("P6")


# Bot 4th
# Pitching: BOS #22 Rick Porcello
b4 = game.new_inning()

# 4. MIN #99 Logan Morrison (X - X - X)
b4.new_ab()
b4.pitch_list("f b s")
b4.out("P5")

# 5. MIN #36 Robbie Grossman (X - X - X)
b4.new_ab()
b4.pitch_list("c b f c")
b4.out("!K")

# 6. MIN #26 Max Kepler (X - X - X)
b4.new_ab()
b4.pitch_list("c b f c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: MIN #44 Kyle Gibson
t5 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.hit(4)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t5.new_ab()
t5.pitch_list("c c")
t5.hit(1)
t5.advance(2, "18 1B")
t5.advance(3, "2 1B")

# 3. BOS #28 J.D. Martinez (X - X - 16)
t5.new_ab()
t5.pitch_list("1")
t5.out("F9")

# 4. BOS #18 Mitch Moreland (X - X - 16)
t5.new_ab()
t5.pitch_list("c b 1 b")
t5.hit(1)
t5.advance(2, "2 1B")

# 5. BOS #2  Xander Bogaerts (X - 16 - 18)
t5.new_ab(is_risp=True)
t5.pitch_list("b c b f")
t5.hit(1)

# 6. BOS #11 Rafael Devers (16 - 18 - 2)
t5.new_ab(is_risp=True)
t5.pitch_list("f f b b f")
t5.out("IF4")

# 7. BOS #12 Brock Holt (16 - 18 - 2)
t5.new_ab(is_risp=True)
t5.pitch_list("c d f d f f")
t5.out("G4-3")


# Bot 5th
# Pitching: BOS #22 Rick Porcello
b5 = game.new_inning()

# 7. MIN #16 Ehire Adrianza (X - X - X)
b5.new_ab()
b5.pitch_list("c f b f f s")
b5.out("K")

# 8. MIN #24 Ryan LaMarre (X - X - X)
b5.new_ab()
b5.pitch_list("b s c b f b")
b5.out("L5")

# 9. MIN #46 Bobby Wilson (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("L7")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: MIN #44 Kyle Gibson
t6 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.reach("HBP")
t6.thrown_out(2, "19 DP6-4-3", 1, 44)

# 9. BOS #19 Jackie Bradley Jr. (X - X - 3)
t6.new_ab()
t6.out("DP6-4-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t6.new_ab()
t6.pitch_list("b b")
t6.out("F9")


# Bot 6th
# Pitching: BOS #22 Rick Porcello
b6 = game.new_inning()

# 1. MIN #7  Joe Mauer (X - X - X)
b6.new_ab()
b6.pitch_list("c s")
b6.out("L9")

# 2. MIN #2  Brian Dozier (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("F8")

# 3. MIN #45 Taylor Motter (X - X - X)
b6.new_ab()
b6.pitch_list("c c b b")
b6.out("P4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: MIN #57 Ryan Pressly
t7 = game.new_inning()

# Pitching change (MIN): #57 Ryan Pressly replaces #44 Kyle Gibson
t7.pitching_substitution(57)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t7.new_ab()
t7.pitch_list("s c f b b f b c")
t7.out("!K")

# 3. BOS #28 J.D. Martinez (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.hit(1)
t7.advance(2, "18 BB")
t7.advance(4, "2 2B")

# 4. BOS #18 Mitch Moreland (X - X - 28)
t7.new_ab()
t7.pitch_list("b c b b b")
t7.reach("BB")
t7.advance(4, "2 2B")

# 5. BOS #2  Xander Bogaerts (X - 28 - 18)
t7.new_ab(is_risp=True)
t7.pitch_list("c s f")
t7.hit(2, rbis=2)
t7.advance(3, "T")
t7.advance(4, "11 G4-3")

# Pitching change (MIN): #55 Taylor Rogers replaces #57 Ryan Pressly
t7.pitching_substitution(55)

# 6. BOS #11 Rafael Devers (2 - X - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c f b d b")
t7.out("G4-3", rbis=1)

# 7. BOS #12 Brock Holt (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G1-3")


# Bot 7th
# Pitching: BOS #22 Rick Porcello
b7 = game.new_inning()

# 4. MIN #99 Logan Morrison (X - X - X)
b7.new_ab()
b7.pitch_list("b f")
b7.out("F9")

# 5. MIN #36 Robbie Grossman (X - X - X)
b7.new_ab()
b7.pitch_list("c f b b")
b7.out("F9")

# 6. MIN #26 Max Kepler (X - X - X)
b7.new_ab()
b7.out("F9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: MIN #38 Matt Belisle
t8 = game.new_inning()

# Pitching change (MIN): #38 Matt Belisle replaces #55 Taylor Rogers
t8.pitching_substitution(38)

# 8. BOS #3  Sandy León (X - X - X)
t8.new_ab()
t8.pitch_list("b c")
t8.hit(1)
t8.advance(4, "16 HR")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 3)
t8.new_ab()
t8.pitch_list("f c b d f b s")
t8.out("K")

# 1. BOS #50 Mookie Betts (X - X - 3)
t8.new_ab()
t8.pitch_list("c")
t8.out("L7")

# 2. BOS #16 Andrew Benintendi (X - X - 3)
t8.new_ab()
t8.pitch_list("c c b")
t8.hit(4, rbis=2)

# 3. BOS #28 J.D. Martinez (X - X - X)
t8.new_ab()
t8.pitch_list("b b c")
t8.hit(2)
t8.advance(4, "18 2B")

# 4. BOS #18 Mitch Moreland (X - 28 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("f")
t8.hit(2, rbis=1)

# 5. BOS #2  Xander Bogaerts (X - 18 - X)
t8.new_ab(is_risp=True)
t8.out("P3")


# Bot 8th
# Pitching: BOS #76 Hector Velázquez
b8 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #22 Rick Porcello
b8.pitching_substitution(76)

# 7. MIN #16 Ehire Adrianza (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.out("F8")

# 8. MIN #24 Ryan LaMarre (X - X - X)
b8.new_ab()
b8.pitch_list("f b b")
b8.hit(1)
b8.thrown_out(2, "46 DP5-4-3", 2, 76)

# 9. MIN #46 Bobby Wilson (X - X - 24)
b8.new_ab()
b8.pitch_list("d c d s")
b8.out("DP5-4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: MIN #68 Matt Magill
t9 = game.new_inning()

# Pitching change (MIN): #68 Matt Magill replaces #38 Matt Belisle
t9.pitching_substitution(68)

# Defensive change (MIN): #23 Mitch Garver replaces #7 Joe Mauer (1B), playing 1B, batting 1st
t9.defensive_substitution(1, 23, "3")

# 6. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("L9")

# 7. BOS #12 Brock Holt (X - X - X)
t9.new_ab()
t9.pitch_list("c s b b b")
t9.hit(2)
t9.advance(4, "19 1B")

# Offensive change (BOS): Pinch-hitter #23 Blake Swihart replaces #3 Sandy León, batting 8th
t9.offensive_substitution(8, 23, "PH")

# 8. BOS #23 Blake Swihart (X - 12 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("b b c f s")
t9.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - 12 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("b s")
t9.hit(1, rbis=1)
t9.advance(2, "50 1B")

# 1. BOS #50 Mookie Betts (X - X - 19)
t9.new_ab()
t9.pitch_list("b s b f")
t9.hit(1)

# 2. BOS #16 Andrew Benintendi (X - 19 - 50)
t9.new_ab(is_risp=True)
t9.pitch_list("f b c b f c")
t9.out("!K")


# Bot 9th
# Pitching: BOS #76 Hector Velázquez
b9 = game.new_inning()

# Defensive switch (BOS): #23 Blake Swihart moves to C
b9.defensive_switch(23, "2")

# 1. MIN #23 Mitch Garver (X - X - X)
b9.new_ab()
b9.pitch_list("c b b b")
b9.hit(1)
b9.advance(3, "2 2B")
b9.advance(4, "45 G4-3")

# 2. MIN #2  Brian Dozier (X - X - 23)
b9.new_ab()
b9.pitch_list("c f")
b9.hit(2)
b9.advance(3, "45 G4-3")
b9.advance(4, "99 SF8")

# 3. MIN #45 Taylor Motter (23 - 2 - X)
b9.new_ab(is_risp=True)
b9.out("G4-3", rbis=1)

# 4. MIN #99 Logan Morrison (2 - X - X)
b9.new_ab(is_risp=True)
b9.pitch_list("b")
b9.out("SF8", rbis=1)

# 5. MIN #36 Robbie Grossman (X - X - X)
b9.new_ab()
b9.pitch_list("b b c")
b9.out("G4-3")

# Winning team: BOS
# WP: BOS #22 Rick Porcello
game.winning_pitcher(22, is_away_team=True)

# Loser team: MIN
# LP: MIN #44 Kyle Gibson
game.losing_pitcher(44)

# print(game)
game.generate_scorecard()
