import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ DET, 2018-07-21
# https://www.baseball-reference.com/boxes/DET/DET201807210.shtml
# https://www.mlb.com/gameday/red-sox-vs-tigers/2018/07/21/530875/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-21 18:10-20:37",
        "at": "Comerica Park, Detroit, MI",
        "att": "31,682",
        "temp": "73F, Overcast",
        "wind": "9mph, In From LF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 61,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                25: "Steve Pearce",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                23: "Blake Swihart",
                # Starting pitcher
                61: "Brian Johnson",
                # Bench
                5: "Tzu-Wei Lin",
                12: "Brock Holt",
                28: "J.D. Martinez",
                3: "Sandy León",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                22: "Rick Porcello",
                41: "Chris Sale",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [61, 41, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [2, "6"],
                [18, "3"],
                [25, "0"],
                [11, "5"],
                [36, "4"],
                [19, "8"],
                [23, "2"],
            ],
            "bench": [
                [5, "OF"],
                [12, "2B"],
                [28, "DH"],
                [3, "C"],
            ],
            "bullpen": [47, 44, 22, 41, 37, 24, 46, 76, 70, 56, 32],
        },
        "home": {
            "team": "Detroit Tigers",
            "starter": 50,
            "roster": {
                # Lineup
                12: "Leonys Martin",
                28: "Niko Goodrum",
                9: "Nick Castellanos",
                55: "John Hicks",
                41: "Victor Martinez",
                46: "Jeimer Candelario",
                60: "Ronny Rodríguez",
                1: "Jose Iglesias",
                21: "JaCoby Jones",
                # Starting pitcher
                50: "Mike Fiers",
                # Bench
                37: "James Adduci",
                22: "Victor Reyes",
                34: "James McCann",
                # Bullpen
                38: "Francisco Liriano",
                30: "Alex Wilson",
                58: "Victor Alcántara",
                19: "Louis Coleman",
                27: "Jordan Zimmermann",
                48: "Matthew Boyd",
                68: "Daniel Stumpf",
                61: "Shane Greene",
                54: "Drew VerHagen",
                45: "Buck Farmer",
                77: "Joe Jiménez",
                36: "Blaine Hardy",
            },
            "lefties": [38, 48, 68, 36],
            "lineup": [
                [12, "8"],
                [28, "4"],
                [9, "9"],
                [55, "2"],
                [41, "0"],
                [46, "5"],
                [60, "3"],
                [1, "6"],
                [21, "7"],
            ],
            "bench": [
                [37, "1B"],
                [22, "RF"],
                [34, "C"],
            ],
            "bullpen": [38, 30, 58, 19, 27, 48, 68, 61, 54, 45, 77, 36],
        },
        "umpires": {
            "HP": "Stu Scheurwater",
            "1B": "Eric Cooper",
            "2B": "Cory Blaser",
            "3B": "Gary Cederstrom",
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
# Pitching: DET #50 Mike Fiers
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c c s")
t1.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("G4-3")

# 3. BOS #2  Xander Bogaerts (X - X - X)
t1.new_ab()
t1.pitch_list("c f s")
t1.out("K")


# Bot 1st
# Pitching: BOS #61 Brian Johnson
b1 = game.new_inning()

# 1. DET #12 Leonys Martin (X - X - X)
b1.new_ab()
b1.pitch_list("b s f f c")
b1.out("!K")

# 2. DET #28 Niko Goodrum (X - X - X)
b1.new_ab()
b1.pitch_list("b s b f t")
b1.out("KT")

# 3. DET #9  Nick Castellanos (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c s")
b1.out("G5-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: DET #50 Mike Fiers
t2 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t2.new_ab()
t2.hit(1)

# 5. BOS #25 Steve Pearce (X - X - 18)
t2.new_ab()
t2.out("F7")

# 6. BOS #11 Rafael Devers (X - X - 18)
t2.new_ab()
t2.pitch_list("c b b s s")
t2.out("K")

# 7. BOS #36 Eduardo Núñez (X - X - 18)
t2.new_ab()
t2.pitch_list("s")
t2.out("G6-3")


# Bot 2nd
# Pitching: BOS #61 Brian Johnson
b2 = game.new_inning()

# 4. DET #55 John Hicks (X - X - X)
b2.new_ab()
b2.out("G6-3")

# 5. DET #41 Victor Martinez (X - X - X)
b2.new_ab()
b2.pitch_list("c c b")
b2.error(5)
b2.reach("E5")
b2.advance(2, "46 1B")
b2.advance("U", "1 2B")

# 6. DET #46 Jeimer Candelario (X - X - 41)
b2.new_ab()
b2.pitch_list("b b f")
b2.hit(1)
b2.advance(3, "1 2B")
b2.advance("U", "1 2B")

# 7. DET #60 Ronny Rodríguez (X - 41 - 46)
b2.new_ab()
b2.pitch_list("b b c c f s")
b2.out("K")

# 8. DET #1  Jose Iglesias (X - 41 - 46)
b2.new_ab()
b2.pitch_list("b c b f")
b2.hit(2, rbis=2)

# 9. DET #21 JaCoby Jones (X - 1 - X)
b2.new_ab()
b2.pitch_list("b f")
b2.out("F9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: DET #50 Mike Fiers
t3 = game.new_inning()

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.out("G6-3")

# 9. BOS #23 Blake Swihart (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c s b")
t3.reach("BB")
t3.advance(2, "16 SB")

# 1. BOS #50 Mookie Betts (X - X - 23)
t3.new_ab()
t3.pitch_list("c 1 1 b f")
t3.out("L8")

# 2. BOS #16 Andrew Benintendi (X - X - 23)
t3.new_ab()
t3.pitch_list("b b c f f b f b")
t3.reach("BB")

# 3. BOS #2  Xander Bogaerts (X - 23 - 16)
t3.new_ab()
t3.pitch_list("b c b")
t3.out("G4-3")


# Bot 3rd
# Pitching: BOS #61 Brian Johnson
b3 = game.new_inning()

# 1. DET #12 Leonys Martin (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("F9")

# 2. DET #28 Niko Goodrum (X - X - X)
b3.new_ab()
b3.pitch_list("b c")
b3.out("F8")

# 3. DET #9  Nick Castellanos (X - X - X)
b3.new_ab()
b3.pitch_list("b b t")
b3.hit(1)
b3.thrown_out(2, "55 FC6-4", 3, 61)

# 4. DET #55 John Hicks (X - X - 9)
b3.new_ab()
b3.pitch_list("1 b f")
b3.reach("FC6-4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: DET #50 Mike Fiers
t4 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.out("P6")

# 5. BOS #25 Steve Pearce (X - X - X)
t4.new_ab()
t4.pitch_list("b b b b")
t4.reach("BB")

# 6. BOS #11 Rafael Devers (X - X - 25)
t4.new_ab()
t4.pitch_list("s f 1 s")
t4.out("K")

# 7. BOS #36 Eduardo Núñez (X - X - 25)
t4.new_ab()
t4.out("G4-3")


# Bot 4th
# Pitching: BOS #61 Brian Johnson
b4 = game.new_inning()

# 5. DET #41 Victor Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("F7")

# 6. DET #46 Jeimer Candelario (X - X - X)
b4.new_ab()
b4.pitch_list("b b c s")
b4.hit(1)
b4.advance(3, "60 1B")

# 7. DET #60 Ronny Rodríguez (X - X - 46)
b4.new_ab()
b4.pitch_list("f")
b4.hit(1)
b4.thrown_out(2, "21 FC5-4", 3, 61)

# 8. DET #1  Jose Iglesias (46 - X - 60)
b4.new_ab()
b4.pitch_list("s f f f 1 b s")
b4.out("K")

# 9. DET #21 JaCoby Jones (46 - X - 60)
b4.new_ab()
b4.pitch_list("c t d 1")
b4.reach("FC5-4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: DET #50 Mike Fiers
t5 = game.new_inning()

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("c b b b")
t5.out("F8")

# 9. BOS #23 Blake Swihart (X - X - X)
t5.new_ab()
t5.pitch_list("f c s")
t5.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("c b b f f b f")
t5.hit(1)
t5.advance(3, "16 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t5.new_ab()
t5.pitch_list("f")
t5.hit(1)

# 3. BOS #2  Xander Bogaerts (50 - X - 16)
t5.new_ab()
t5.pitch_list("c f s")
t5.out("K")


# Bot 5th
# Pitching: BOS #61 Brian Johnson
b5 = game.new_inning()

# 1. DET #12 Leonys Martin (X - X - X)
b5.new_ab()
b5.out("F8")

# 2. DET #28 Niko Goodrum (X - X - X)
b5.new_ab()
b5.pitch_list("c s b s")
b5.out("K")

# 3. DET #9  Nick Castellanos (X - X - X)
b5.new_ab()
b5.pitch_list("f")
b5.out("G6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: DET #50 Mike Fiers
t6 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t6.new_ab()
t6.pitch_list("c s")
t6.out("F7")

# 5. BOS #25 Steve Pearce (X - X - X)
t6.new_ab()
t6.pitch_list("c b b b")
t6.out("(F)F7")

# 6. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("b c f")
t6.hit(1)
t6.advance(2, "36 1B")

# 7. BOS #36 Eduardo Núñez (X - X - 11)
t6.new_ab()
t6.pitch_list("b")
t6.hit(1)

# 8. BOS #19 Jackie Bradley Jr. (X - 11 - 36)
t6.new_ab()
t6.out("F7")


# Bot 6th
# Pitching: BOS #47 Tyler Thornburg
b6 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #61 Brian Johnson
b6.pitching_substitution(47)

# 4. DET #55 John Hicks (X - X - X)
b6.new_ab()
b6.pitch_list("f b b f b b")
b6.reach("BB")
b6.advance(3, "41 1B")
b6.advance(4, "46 SF7")

# 5. DET #41 Victor Martinez (X - X - 55)
b6.new_ab()
b6.hit(1)
b6.advance(2, "46 SF7")
b6.advance(3, "60 WP")
b6.advance(4, "1 HR")

# 6. DET #46 Jeimer Candelario (55 - X - 41)
b6.new_ab()
b6.pitch_list("c d")
b6.out("SF7", rbis=1)

# 7. DET #60 Ronny Rodríguez (X - 41 - X)
b6.new_ab()
b6.pitch_list("b b")
b6.wp()
b6.out("G6-3")

# 8. DET #1  Jose Iglesias (41 - X - X)
b6.new_ab()
b6.pitch_list("d c c")
b6.hit(4, rbis=2)

# 9. DET #21 JaCoby Jones (X - X - X)
b6.new_ab()
b6.pitch_list("b f s c")
b6.out("!K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: DET #50 Mike Fiers
t7 = game.new_inning()

# 9. BOS #23 Blake Swihart (X - X - X)
t7.new_ab()
t7.pitch_list("c b f b")
t7.out("G3")

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.pitch_list("b c")
t7.hit(1)
t7.advance(3, "16 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t7.new_ab()
t7.pitch_list("b c b")
t7.hit(1)
t7.thrown_out(2, "2 DP5-4-3", 2, 30)

# Pitching change (DET): #30 Alex Wilson replaces #50 Mike Fiers
t7.pitching_substitution(30)

# 3. BOS #2  Xander Bogaerts (50 - X - 16)
t7.new_ab()
t7.pitch_list("c")
t7.out("DP5-4-3")


# Bot 7th
# Pitching: BOS #70 Ryan Brasier
b7 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #47 Tyler Thornburg
b7.pitching_substitution(70)

# 1. DET #12 Leonys Martin (X - X - X)
b7.new_ab()
b7.pitch_list("f f b f s")
b7.out("K")

# 2. DET #28 Niko Goodrum (X - X - X)
b7.new_ab()
b7.pitch_list("t f f b s")
b7.out("K")

# 3. DET #9  Nick Castellanos (X - X - X)
b7.new_ab()
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: DET #30 Alex Wilson
t8 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t8.new_ab()
t8.out("G3")

# 5. BOS #25 Steve Pearce (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.out("F8")

# 6. BOS #11 Rafael Devers (X - X - X)
t8.new_ab()
t8.pitch_list("c b b")
t8.out("G5-3")


# Bot 8th
# Pitching: BOS #76 Hector Velázquez
b8 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #70 Ryan Brasier
b8.pitching_substitution(76)

# 4. DET #55 John Hicks (X - X - X)
b8.new_ab()
b8.pitch_list("b b f b f c")
b8.out("!K")

# 5. DET #41 Victor Martinez (X - X - X)
b8.new_ab()
b8.pitch_list("b s")
b8.out("F8")

# 6. DET #46 Jeimer Candelario (X - X - X)
b8.new_ab()
b8.pitch_list("b s b s")
b8.out("G5-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: DET #61 Shane Greene
t9 = game.new_inning()

# Pitching change (DET): #61 Shane Greene replaces #30 Alex Wilson
t9.pitching_substitution(61)

# 7. BOS #36 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("c b b f c")
t9.out("!K")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("s s b f b s")
t9.out("K")

# 9. BOS #23 Blake Swihart (X - X - X)
t9.new_ab()
t9.hit(1)
t9.advance(2, "50 DI")

# 1. BOS #50 Mookie Betts (X - X - 23)
t9.new_ab()
t9.pitch_list("c b s b d")
t9.out("G6-3")

# Winning team: DET
# WP: DET #50 Mike Fiers
game.winning_pitcher(50)

# Loser team: BOS
# LP: BOS #61 Brian Johnson
game.losing_pitcher(61, is_away_team=True)

# print(game)
game.generate_scorecard()
