import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ DET, 2018-07-22
# https://www.baseball-reference.com/boxes/DET/DET201807220.shtml
# https://www.mlb.com/gameday/red-sox-vs-tigers/2018/07/22/530890/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-22 14:45-17:40",
        "at": "Comerica Park, Detroit, MI",
        "att": "25,012",
        "temp": "68F, Rain",
        "wind": "13mph, L To R",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                25: "Steve Pearce",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                3: "Sandy León",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                5: "Tzu-Wei Lin",
                18: "Mitch Moreland",
                12: "Brock Holt",
                23: "Blake Swihart",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                22: "Rick Porcello",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [41, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [25, "3"],
                [2, "6"],
                [11, "5"],
                [36, "4"],
                [19, "8"],
                [3, "2"],
            ],
            "bench": [
                [5, "OF"],
                [18, "1B"],
                [12, "2B"],
                [23, "C"],
            ],
            "bullpen": [47, 44, 22, 61, 37, 24, 46, 76, 70, 56, 32],
        },
        "home": {
            "team": "Detroit Tigers",
            "starter": 36,
            "roster": {
                # Lineup
                60: "Ronny Rodríguez",
                28: "Niko Goodrum",
                9: "Nick Castellanos",
                55: "John Hicks",
                46: "Jeimer Candelario",
                34: "James McCann",
                21: "JaCoby Jones",
                1: "Jose Iglesias",
                22: "Victor Reyes",
                # Starting pitcher
                36: "Blaine Hardy",
                # Bench
                41: "Victor Martinez",
                37: "James Adduci",
                12: "Leonys Martin",
                # Bullpen
                38: "Francisco Liriano",
                30: "Alex Wilson",
                58: "Victor Alcántara",
                50: "Mike Fiers",
                19: "Louis Coleman",
                27: "Jordan Zimmermann",
                48: "Matthew Boyd",
                68: "Daniel Stumpf",
                61: "Shane Greene",
                54: "Drew VerHagen",
                45: "Buck Farmer",
                77: "Joe Jiménez",
            },
            "lefties": [36, 38, 48, 68],
            "lineup": [
                [60, "4"],
                [28, "9"],
                [9, "0"],
                [55, "3"],
                [46, "5"],
                [34, "2"],
                [21, "8"],
                [1, "6"],
                [22, "7"],
            ],
            "bench": [
                [41, "DH"],
                [37, "1B"],
                [12, "CF"],
            ],
            "bullpen": [38, 30, 58, 50, 19, 27, 48, 68, 61, 54, 45, 77],
        },
        "umpires": {
            "HP": "Eric Cooper",
            "1B": "Cory Blaser",
            "2B": "Gary Cederstrom",
            "3B": "Stu Scheurwater",
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
# Pitching: DET #36 Blaine Hardy
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c b s c")
t1.out("!K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b s f")
t1.out("G4-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
t1.new_ab()
t1.pitch_list("f b b s f c")
t1.out("!K")


# Bot 1st
# Pitching: BOS #41 Chris Sale
b1 = game.new_inning()

# 1. DET #60 Ronny Rodríguez (X - X - X)
b1.new_ab()
b1.pitch_list("b f")
b1.out("G5-3")

# 2. DET #28 Niko Goodrum (X - X - X)
b1.new_ab()
b1.pitch_list("f")
b1.out("F9")

# 3. DET #9  Nick Castellanos (X - X - X)
b1.new_ab()
b1.pitch_list("s b c f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: DET #36 Blaine Hardy
t2 = game.new_inning()

# 4. BOS #25 Steve Pearce (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.hit(1)
t2.advance(3, "2 2B")
t2.advance(4, "11 G4-3")

# 5. BOS #2  Xander Bogaerts (X - X - 25)
t2.new_ab()
t2.pitch_list("c f 1 f b b")
t2.hit(2)
t2.advance(3, "11 G4-3")
t2.advance(4, "36 G6-3")

# 6. BOS #11 Rafael Devers (25 - 2 - X)
t2.new_ab()
t2.out("G4-3", rbis=1)

# 7. BOS #36 Eduardo Núñez (2 - X - X)
t2.new_ab()
t2.out("G6-3", rbis=1)

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t2.new_ab()
t2.pitch_list("f")
t2.hit(1)

# 9. BOS #3  Sandy León (X - X - 19)
t2.new_ab()
t2.pitch_list("c 1 c f")
t2.out("F7")


# Bot 2nd
# Pitching: BOS #41 Chris Sale
b2 = game.new_inning()

# 4. DET #55 John Hicks (X - X - X)
b2.new_ab()
b2.pitch_list("c c s")
b2.out("K")

# 5. DET #46 Jeimer Candelario (X - X - X)
b2.new_ab()
b2.pitch_list("b c c f f b f b f f f")
b2.out("G5-3")

# 6. DET #34 James McCann (X - X - X)
b2.new_ab()
b2.pitch_list("c c s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: DET #36 Blaine Hardy
t3 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c f")
t3.out("P4")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("c b b b s s")
t3.out("K")

# 3. BOS #28 J.D. Martinez (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("G5-3")


# Bot 3rd
# Pitching: BOS #41 Chris Sale
b3 = game.new_inning()

# 7. DET #21 JaCoby Jones (X - X - X)
b3.new_ab()
b3.pitch_list("s f b f s")
b3.out("K")

# 8. DET #1  Jose Iglesias (X - X - X)
b3.new_ab()
b3.pitch_list("c s f")
b3.out("G4-3")

# 9. DET #22 Victor Reyes (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(1)

# 1. DET #60 Ronny Rodríguez (X - X - 22)
b3.new_ab()
b3.pitch_list("f s b")
b3.out("F9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: DET #36 Blaine Hardy
t4 = game.new_inning()

# 4. BOS #25 Steve Pearce (X - X - X)
t4.new_ab()
t4.pitch_list("b f b b c f")
t4.hit(1)
t4.advance(3, "2 2B")
t4.advance(4, "36 1B")

# 5. BOS #2  Xander Bogaerts (X - X - 25)
t4.new_ab()
t4.pitch_list("c 1")
t4.hit(2)
t4.advance(3, "36 1B")
t4.advance(4, "19 HR")

# 6. BOS #11 Rafael Devers (25 - 2 - X)
t4.new_ab()
t4.reach("FC3")
t4.thrown_out(3, "36 5", 1, 54)
t4.advance(2, "36 1B")

# Pitching change (DET): #54 Drew VerHagen replaces #36 Blaine Hardy
t4.pitching_substitution(54)

# 7. BOS #36 Eduardo Núñez (25 - 2 - 11)
t4.new_ab()
t4.pitch_list("b")
t4.hit(1, rbis=1)
t4.advance(4, "19 HR")

# 8. BOS #19 Jackie Bradley Jr. (2 - X - 36)
t4.new_ab()
t4.pitch_list("b f b c 1 1 f")
t4.hit(4, rbis=3)

# 9. BOS #3  Sandy León (X - X - X)
t4.new_ab()
t4.pitch_list("c b s b s")
t4.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t4.new_ab()
t4.pitch_list("b c c b")
t4.out("G6-3")


# Bot 4th
# Pitching: BOS #41 Chris Sale
b4 = game.new_inning()

# 2. DET #28 Niko Goodrum (X - X - X)
b4.new_ab()
b4.pitch_list("c b s s")
b4.out("K")

# 3. DET #9  Nick Castellanos (X - X - X)
b4.new_ab()
b4.pitch_list("t b f")
b4.hit(2)

# 4. DET #55 John Hicks (X - 9 - X)
b4.new_ab()
b4.pitch_list("s f f b f b b t")
b4.out("KT")

# 5. DET #46 Jeimer Candelario (X - 9 - X)
b4.new_ab()
b4.pitch_list("c s b f f f f b")
b4.out("G5-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: DET #54 Drew VerHagen
t5 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t5.new_ab()
t5.pitch_list("c b f")
t5.out("F8")

# 3. BOS #28 J.D. Martinez (X - X - X)
t5.new_ab()
t5.pitch_list("b b f")
t5.out("F9")

# 4. BOS #25 Steve Pearce (X - X - X)
t5.new_ab()
t5.pitch_list("c c f b f s")
t5.out("K2-3")


# Bot 5th
# Pitching: BOS #41 Chris Sale
b5 = game.new_inning()

# 6. DET #34 James McCann (X - X - X)
b5.new_ab()
b5.pitch_list("b f f")
b5.out("F9")

# 7. DET #21 JaCoby Jones (X - X - X)
b5.new_ab()
b5.pitch_list("c s s")
b5.out("K")

# 8. DET #1  Jose Iglesias (X - X - X)
b5.new_ab()
b5.pitch_list("b b c f f")
b5.reach("HBP")

# 9. DET #22 Victor Reyes (X - X - 1)
b5.new_ab()
b5.pitch_list("b b t")
b5.out("L9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: DET #54 Drew VerHagen
t6 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t6.new_ab()
t6.pitch_list("b b c f b")
t6.out("F9")

# 6. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("b s b f f c")
t6.out("!K")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t6.new_ab()
t6.pitch_list("f")
t6.out("G1-3")


# Bot 6th
# Pitching: BOS #41 Chris Sale
b6 = game.new_inning()

# 1. DET #60 Ronny Rodríguez (X - X - X)
b6.new_ab()
b6.pitch_list("c b f f b b s")
b6.out("K")

# 2. DET #28 Niko Goodrum (X - X - X)
b6.new_ab()
b6.pitch_list("c b f b c")
b6.out("!K")

# 3. DET #9  Nick Castellanos (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: DET #68 Daniel Stumpf
t7 = game.new_inning()

# Pitching change (DET): #68 Daniel Stumpf replaces #54 Drew VerHagen
t7.pitching_substitution(68)

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("b c s b s")
t7.out("K")

# 9. BOS #3  Sandy León (X - X - X)
t7.new_ab()
t7.pitch_list("s b b f b d")
t7.reach("BB")
t7.advance(2, "50 1B")
t7.advance(4, "16 3B")

# 1. BOS #50 Mookie Betts (X - X - 3)
t7.new_ab()
t7.pitch_list("c b d b f f")
t7.hit(1)
t7.advance(4, "16 3B")

# 2. BOS #16 Andrew Benintendi (X - 3 - 50)
t7.new_ab()
t7.pitch_list("c b")
t7.hit(3, rbis=2)
t7.advance(4, "28 SF9")

# Pitching change (DET): #19 Louis Coleman replaces #68 Daniel Stumpf
t7.pitching_substitution(19)

# 3. BOS #28 J.D. Martinez (16 - X - X)
t7.new_ab()
t7.pitch_list("c f")
t7.out("SF9", rbis=1)

# 4. BOS #25 Steve Pearce (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("F9")


# Bot 7th
# Pitching: BOS #44 Brandon Workman
b7 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #41 Chris Sale
b7.pitching_substitution(44)

# Defensive change (BOS): #5 Tzu-Wei Lin replaces #2 Xander Bogaerts (SS), playing SS, batting 5th
b7.defensive_substitution(5, 5, "6")

# 4. DET #55 John Hicks (X - X - X)
b7.new_ab()
b7.pitch_list("b f b s f")
b7.out("P1")

# 5. DET #46 Jeimer Candelario (X - X - X)
b7.new_ab()
b7.pitch_list("b b c b")
b7.hit(4, rbis=1)

# 6. DET #34 James McCann (X - X - X)
b7.new_ab()
b7.pitch_list("c b b c f b")
b7.hit(1)
b7.thrown_out(3, "1 4-6", 3, 44)
b7.advance(2, "1 1B")

# 7. DET #21 JaCoby Jones (X - X - 34)
b7.new_ab()
b7.pitch_list("f")
b7.out("F9")

# 8. DET #1  Jose Iglesias (X - X - 34)
b7.new_ab()
b7.pitch_list("c c")
b7.hit(1)


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: DET #19 Louis Coleman
t8 = game.new_inning()

# 5. BOS #5  Tzu-Wei Lin (X - X - X)
t8.new_ab()
t8.out("(F)P5")

# 6. BOS #11 Rafael Devers (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.out("P3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t8.new_ab()
t8.pitch_list("b b f")
t8.out("F8")


# Bot 8th
# Pitching: BOS #56 Joe Kelly
b8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #44 Brandon Workman
b8.pitching_substitution(56)

# 9. DET #22 Victor Reyes (X - X - X)
b8.new_ab()
b8.pitch_list("f t b")
b8.error(6)
b8.reach("E6")
b8.thrown_out(2, "60 FC4-6", 1, 56)

# 1. DET #60 Ronny Rodríguez (X - X - 22)
b8.new_ab()
b8.pitch_list("b")
b8.reach("FC4-6")
b8.advance(2, "28 BB")
b8.advance(3, "55 BB")

# 2. DET #28 Niko Goodrum (X - X - 60)
b8.new_ab()
b8.pitch_list("d f b b b")
b8.reach("BB")
b8.advance(2, "55 BB")

# Offensive change (DET): Pinch-hitter #37 James Adduci replaces #9 Nick Castellanos, batting 3rd
b8.offensive_substitution(3, 37, "PH")

# 3. DET #37 James Adduci (X - 60 - 28)
b8.new_ab()
b8.out("L6")

# 4. DET #55 John Hicks (X - 60 - 28)
b8.new_ab()
b8.pitch_list("b b c b b")
b8.reach("BB")

# 5. DET #46 Jeimer Candelario (60 - 28 - 55)
b8.new_ab()
b8.pitch_list("b b f b c f f")
b8.out("F8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: DET #45 Buck Farmer
t9 = game.new_inning()

# Pitching change (DET): #45 Buck Farmer replaces #19 Louis Coleman
t9.pitching_substitution(45)

# Defensive switch (DET): #37 James Adduci moves to DH
t9.defensive_switch(37, "0")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("b s b b")
t9.out("L9")

# 9. BOS #3  Sandy León (X - X - X)
t9.new_ab()
t9.pitch_list("b c b s f s")
t9.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t9.new_ab()
t9.pitch_list("b f c b b")
t9.out("F8")


# Bot 9th
# Pitching: BOS #47 Tyler Thornburg
b9 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #56 Joe Kelly
b9.pitching_substitution(47)

# 6. DET #34 James McCann (X - X - X)
b9.new_ab()
b9.out("P3")

# 7. DET #21 JaCoby Jones (X - X - X)
b9.new_ab()
b9.pitch_list("c f s")
b9.out("K")

# 8. DET #1  Jose Iglesias (X - X - X)
b9.new_ab()
b9.pitch_list("s c")
b9.out("P4")

# Winning team: BOS
# WP: BOS #41 Chris Sale
game.winning_pitcher(41, is_away_team=True)

# Loser team: DET
# LP: DET #36 Blaine Hardy
game.losing_pitcher(36)

# print(game)
game.generate_scorecard()
