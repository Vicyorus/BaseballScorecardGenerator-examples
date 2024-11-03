import os
from baseball_scorecard.baseball_scorecard import Scorecard

# DET @ BOS, 2018-06-07
# https://www.baseball-reference.com/boxes/BOS/BOS201806070.shtml
# https://www.mlb.com/gameday/tigers-vs-red-sox/2018/06/07/530336/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-07 19:10-22:05",
        "at": "Fenway Park, Boston, MA",
        "att": "36,556",
        "temp": "67F, Cloudy",
        "wind": "14mph, Out To LF",
        "away": {
            "team": "Detroit Tigers",
            "starter": 48,
            "roster": {
                # Lineup
                21: "JaCoby Jones",
                9: "Nick Castellanos",
                24: "Miguel Cabrera",
                41: "Victor Martinez",
                46: "Jeimer Candelario",
                55: "John Hicks",
                12: "Leonys Martin",
                1: "Jose Iglesias",
                49: "Dixon Machado",
                # Starting pitcher
                48: "Matthew Boyd",
                # Bench
                28: "Niko Goodrum",
                22: "Victor Reyes",
                34: "James McCann",
                # Bullpen
                30: "Alex Wilson",
                50: "Mike Fiers",
                19: "Louis Coleman",
                26: "Zac Reininger",
                53: "Warwick Saupold",
                57: "Artie Lewicki",
                61: "Shane Greene",
                54: "Drew VerHagen",
                45: "Buck Farmer",
                32: "Michael Fulmer",
                77: "Joe Jiménez",
                36: "Blaine Hardy",
            },
            "lefties": [48, 36],
            "lineup": [
                [21, "7"],
                [9, "9"],
                [24, "3"],
                [41, "0"],
                [46, "5"],
                [55, "2"],
                [12, "8"],
                [1, "6"],
                [49, "4"],
            ],
            "bench": [
                [28, "3B"],
                [22, "RF"],
                [34, "C"],
            ],
            "bullpen": [30, 50, 19, 26, 53, 57, 61, 54, 45, 32, 77, 36],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 68,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                59: "Sam Travis",
                11: "Rafael Devers",
                7: "Christian Vázquez",
                23: "Blake Swihart",
                # Starting pitcher
                68: "Jalen Beeks",
                # Bench
                12: "Brock Holt",
                19: "Jackie Bradley Jr.",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [68, 57, 41, 61, 24],
            "lineup": [
                [16, "8"],
                [2, "6"],
                [28, "9"],
                [18, "3"],
                [36, "4"],
                [59, "7"],
                [11, "5"],
                [7, "0"],
                [23, "2"],
            ],
            "bench": [
                [12, "2B"],
                [19, "CF"],
                [3, "C"],
            ],
            "bullpen": [57, 35, 44, 22, 41, 61, 37, 24, 46, 76, 56, 32],
        },
        "umpires": {
            "HP": "Jeremie Rehak",
            "1B": "Mark Wegner",
            "2B": "John Tumpane",
            "3B": "Mike DiMuro",
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
# Pitching: BOS #68 Jalen Beeks
t1 = game.new_inning()

# 1. DET #21 JaCoby Jones (X - X - X)
t1.new_ab()
t1.pitch_list("c b b f t")
t1.out("KT")

# 2. DET #9  Nick Castellanos (X - X - X)
t1.new_ab()
t1.pitch_list("b s b f f")
t1.hit(2)
t1.advance(3, "41 F9")
t1.advance(4, "46 2B")

# 3. DET #24 Miguel Cabrera (X - 9 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b f b b f b")
t1.reach("BB")
t1.advance(3, "46 2B")
t1.advance(4, "55 1B")

# 4. DET #41 Victor Martinez (X - 9 - 24)
t1.new_ab(is_risp=True)
t1.pitch_list("c f")
t1.out("F9")

# 5. DET #46 Jeimer Candelario (9 - X - 24)
t1.new_ab(is_risp=True)
t1.pitch_list("d c")
t1.hit(2, rbis=1)
t1.advance(4, "55 1B")

# 6. DET #55 John Hicks (24 - 46 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b b")
t1.hit(1, rbis=2)
t1.advance(4, "12 HR")

# 7. DET #12 Leonys Martin (X - X - 55)
t1.new_ab()
t1.pitch_list("b 1 t")
t1.hit(4, rbis=2)

# 8. DET #1  Jose Iglesias (X - X - X)
t1.new_ab()
t1.pitch_list("b b c")
t1.out("P3")


# Bot 1st
# Pitching: DET #48 Matthew Boyd
b1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b f b b")
b1.hit(4)

# 2. BOS #2  Xander Bogaerts (X - X - X)
b1.new_ab()
b1.pitch_list("c c b c")
b1.out("!K")

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("b b b b")
b1.reach("BB")
b1.advance(2, "36 WP")

# 4. BOS #18 Mitch Moreland (X - X - 28)
b1.new_ab()
b1.pitch_list("b c f b t")
b1.out("KT")

# 5. BOS #36 Eduardo Núñez (X - X - 28)
b1.new_ab(is_risp=True)
b1.pitch_list("b c b")
b1.wp()
b1.out("F8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #68 Jalen Beeks
t2 = game.new_inning()

# 9. DET #49 Dixon Machado (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.hit(1)
t2.advance(2, "24 BB")
t2.advance(3, "41 BB")

# 1. DET #21 JaCoby Jones (X - X - 49)
t2.new_ab()
t2.pitch_list("f s d b f 1 f c")
t2.out("!K")

# 2. DET #9  Nick Castellanos (X - X - 49)
t2.new_ab()
t2.pitch_list("f")
t2.out("L5")

# 3. DET #24 Miguel Cabrera (X - X - 49)
t2.new_ab()
t2.pitch_list("b d c b c b")
t2.reach("BB")
t2.advance(2, "41 BB")

# 4. DET #41 Victor Martinez (X - 49 - 24)
t2.new_ab(is_risp=True)
t2.pitch_list("c f f b b b f f b")
t2.reach("BB")
t2.thrown_out(2, "46 FC6-4", 3, 68)

# 5. DET #46 Jeimer Candelario (49 - 24 - 41)
t2.new_ab(is_risp=True)
t2.pitch_list("c")
t2.reach("FC6-4")


# Bot 2nd
# Pitching: DET #48 Matthew Boyd
b2 = game.new_inning()

# 6. BOS #59 Sam Travis (X - X - X)
b2.new_ab()
b2.pitch_list("c c b f b f b b")
b2.reach("BB")
b2.advance(2, "11 1B")
b2.advance(3, "23 WP")

# 7. BOS #11 Rafael Devers (X - X - 59)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)
b2.advance(2, "23 WP")

# 8. BOS #7  Christian Vázquez (X - 59 - 11)
b2.new_ab(is_risp=True)
b2.pitch_list("c f s")
b2.out("K")

# 9. BOS #23 Blake Swihart (X - 59 - 11)
b2.new_ab(is_risp=True)
b2.pitch_list("b b b b")
b2.wp()
b2.reach("BB")
b2.thrown_out(2, "16 DP6-3", 2, 48)

# 1. BOS #16 Andrew Benintendi (59 - 11 - 23)
b2.new_ab(is_risp=True)
b2.pitch_list("b")
b2.out("DP6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #68 Jalen Beeks
t3 = game.new_inning()

# 6. DET #55 John Hicks (X - X - X)
t3.new_ab()
t3.pitch_list("b t")
t3.out("P3")

# 7. DET #12 Leonys Martin (X - X - X)
t3.new_ab()
t3.pitch_list("b c")
t3.hit(3)
t3.advance(4, "1 2B")

# 8. DET #1  Jose Iglesias (12 - X - X)
t3.new_ab(is_risp=True)
t3.pitch_list("f b")
t3.hit(2, rbis=1)

# 9. DET #49 Dixon Machado (X - 1 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c s")
t3.out("F7")

# 1. DET #21 JaCoby Jones (X - 1 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("s c s")
t3.out("K")


# Bot 3rd
# Pitching: DET #48 Matthew Boyd
b3 = game.new_inning()

# 2. BOS #2  Xander Bogaerts (X - X - X)
b3.new_ab()
b3.pitch_list("c b b f")
b3.out("P4")

# 3. BOS #28 J.D. Martinez (X - X - X)
b3.new_ab()
b3.out("L7")

# 4. BOS #18 Mitch Moreland (X - X - X)
b3.new_ab()
b3.pitch_list("s s b")
b3.hit(2)

# 5. BOS #36 Eduardo Núñez (X - 18 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("s b f")
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #68 Jalen Beeks
t4 = game.new_inning()

# 2. DET #9  Nick Castellanos (X - X - X)
t4.new_ab()
t4.pitch_list("c f")
t4.out("G6-3")

# 3. DET #24 Miguel Cabrera (X - X - X)
t4.new_ab()
t4.pitch_list("b f c b b c")
t4.out("!K")

# 4. DET #41 Victor Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("f f")
t4.out("F7")


# Bot 4th
# Pitching: DET #48 Matthew Boyd
b4 = game.new_inning()

# 6. BOS #59 Sam Travis (X - X - X)
b4.new_ab()
b4.pitch_list("c b b")
b4.out("L7")

# 7. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.pitch_list("c b b b f")
b4.out("L8")

# 8. BOS #7  Christian Vázquez (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("F9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #61 Brian Johnson
t5 = game.new_inning()

# Pitching change (BOS): #61 Brian Johnson replaces #68 Jalen Beeks
t5.pitching_substitution(61)

# 5. DET #46 Jeimer Candelario (X - X - X)
t5.new_ab()
t5.pitch_list("b c c s")
t5.out("K")

# 6. DET #55 John Hicks (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("L8")

# 7. DET #12 Leonys Martin (X - X - X)
t5.new_ab()
t5.pitch_list("c f f s")
t5.out("K")


# Bot 5th
# Pitching: DET #48 Matthew Boyd
b5 = game.new_inning()

# 9. BOS #23 Blake Swihart (X - X - X)
b5.new_ab()
b5.hit(2)
b5.advance(3, "2 WP")
b5.advance(4, "2 G6-3")

# 1. BOS #16 Andrew Benintendi (X - 23 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c b")
b5.out("(F)P5")

# 2. BOS #2  Xander Bogaerts (X - 23 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b b")
b5.wp()
b5.out("G6-3", rbis=1)

# 3. BOS #28 J.D. Martinez (X - X - X)
b5.new_ab()
b5.pitch_list("s c s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #61 Brian Johnson
t6 = game.new_inning()

# 8. DET #1  Jose Iglesias (X - X - X)
t6.new_ab()
t6.pitch_list("c f f f")
t6.out("G6-3")

# 9. DET #49 Dixon Machado (X - X - X)
t6.new_ab()
t6.pitch_list("b b b c f")
t6.out("G6-3")

# 1. DET #21 JaCoby Jones (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G1-3")


# Bot 6th
# Pitching: DET #48 Matthew Boyd
b6 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
b6.new_ab()
b6.pitch_list("b c b b s s")
b6.out("K")

# 5. BOS #36 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("c f")
b6.out("G4-3")

# 6. BOS #59 Sam Travis (X - X - X)
b6.new_ab()
b6.pitch_list("f f b b b f")
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #61 Brian Johnson
t7 = game.new_inning()

# 2. DET #9  Nick Castellanos (X - X - X)
t7.new_ab()
t7.pitch_list("f")
t7.out("G5-3")

# 3. DET #24 Miguel Cabrera (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G5-3")

# 4. DET #41 Victor Martinez (X - X - X)
t7.new_ab()
t7.pitch_list("c s t")
t7.out("KT")


# Bot 7th
# Pitching: DET #48 Matthew Boyd
b7 = game.new_inning()

# 7. BOS #11 Rafael Devers (X - X - X)
b7.new_ab()
b7.pitch_list("f s s")
b7.out("K2-3")

# 8. BOS #7  Christian Vázquez (X - X - X)
b7.new_ab()
b7.pitch_list("c b b b b")
b7.reach("BB")
b7.advance(2, "23 G3")

# Pitching change (DET): #30 Alex Wilson replaces #48 Matthew Boyd
b7.pitching_substitution(30)

# 9. BOS #23 Blake Swihart (X - X - 7)
b7.new_ab()
b7.pitch_list("b b")
b7.out("G3")

# 1. BOS #16 Andrew Benintendi (X - 7 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c b f")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #61 Brian Johnson
t8 = game.new_inning()

# Defensive change (BOS): #12 Brock Holt replaces #28 J.D. Martinez (RF), playing RF, batting 3rd
t8.defensive_substitution(3, 12, "9")

# 5. DET #46 Jeimer Candelario (X - X - X)
t8.new_ab()
t8.pitch_list("b f f f b f")
t8.hit(1)
t8.advance(2, "55 1B")
t8.advance(4, "1 1B")

# 6. DET #55 John Hicks (X - X - 46)
t8.new_ab()
t8.pitch_list("c b f")
t8.hit(1)
t8.advance(2, "1 1B")
t8.advance(3, "49 FC6-4")

# 7. DET #12 Leonys Martin (X - 46 - 55)
t8.new_ab(is_risp=True)
t8.pitch_list("d f s s")
t8.out("K")

# 8. DET #1  Jose Iglesias (X - 46 - 55)
t8.new_ab(is_risp=True)
t8.pitch_list("f b")
t8.hit(1, rbis=1)
t8.thrown_out(2, "49 FC6-4", 2, 61)

# 9. DET #49 Dixon Machado (X - 55 - 1)
t8.new_ab(is_risp=True)
t8.pitch_list("b s")
t8.reach("FC6-4")

# 1. DET #21 JaCoby Jones (55 - X - 49)
t8.new_ab(is_risp=True)
t8.pitch_list("t b c b s")
t8.out("K")


# Bot 8th
# Pitching: DET #77 Joe Jiménez
b8 = game.new_inning()

# Pitching change (DET): #77 Joe Jiménez replaces #30 Alex Wilson
b8.pitching_substitution(77)

# 2. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("b f b b")
b8.out("P6")

# 3. BOS #12 Brock Holt (X - X - X)
b8.new_ab()
b8.hit(1)
b8.advance(2, "18 BB")
b8.advance(3, "36 1B")

# 4. BOS #18 Mitch Moreland (X - X - 12)
b8.new_ab()
b8.pitch_list("b d b c b")
b8.reach("BB")
b8.advance(2, "36 1B")

# 5. BOS #36 Eduardo Núñez (X - 12 - 18)
b8.new_ab(is_risp=True)
b8.pitch_list("b f")
b8.hit(1)

# 6. BOS #59 Sam Travis (12 - 18 - 36)
b8.new_ab(is_risp=True)
b8.pitch_list("c b s s")
b8.out("K")

# 7. BOS #11 Rafael Devers (12 - 18 - 36)
b8.new_ab(is_risp=True)
b8.pitch_list("b f f f c")
b8.out("!K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #76 Hector Velázquez
t9 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #61 Brian Johnson
t9.pitching_substitution(76)

# 2. DET #9  Nick Castellanos (X - X - X)
t9.new_ab()
t9.pitch_list("f c f b s")
t9.out("K")

# 3. DET #24 Miguel Cabrera (X - X - X)
t9.new_ab()
t9.pitch_list("c b s b")
t9.out("G5-3")

# 4. DET #41 Victor Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("f f c")
t9.out("!K")


# Bot 9th
# Pitching: DET #61 Shane Greene
b9 = game.new_inning()

# Pitching change (DET): #61 Shane Greene replaces #77 Joe Jiménez
b9.pitching_substitution(61)

# 8. BOS #7  Christian Vázquez (X - X - X)
b9.new_ab()
b9.pitch_list("b c")
b9.out("F8")

# 9. BOS #23 Blake Swihart (X - X - X)
b9.new_ab()
b9.pitch_list("c b")
b9.out("F8")

# 1. BOS #16 Andrew Benintendi (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.hit(1)
b9.advance(2, "2 DI")

# 2. BOS #2  Xander Bogaerts (X - X - 16)
b9.new_ab(is_risp=True)
b9.pitch_list("c")
b9.out("G1-4-3")

# Winning team: DET
# WP: DET #48 Matthew Boyd
game.winning_pitcher(48, is_away_team=True)

# Loser team: BOS
# LP: BOS #68 Jalen Beeks
game.losing_pitcher(68)

# print(game)
game.generate_scorecard()
