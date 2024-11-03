import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ KCR, 2018-07-06
# https://www.baseball-reference.com/boxes/KCA/KCA201807060.shtml
# https://www.mlb.com/gameday/red-sox-vs-royals/2018/07/06/530718/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-06 20:15-23:14",
        "at": "Kauffman Stadium, Kansas City, MO",
        "att": "24,673",
        "temp": "90F, Clear",
        "wind": "10mph, In From RF",
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
                12: "Brock Holt",
                36: "Eduardo Núñez",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                11: "Rafael Devers",
                23: "Blake Swihart",
                18: "Mitch Moreland",
                7: "Christian Vázquez",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                24: "David Price",
                44: "Brandon Workman",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                22: "Rick Porcello",
                56: "Joe Kelly",
                32: "Matt Barnes",
                37: "Heath Hembree",
            },
            "lefties": [41, 57, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [25, "3"],
                [2, "6"],
                [12, "4"],
                [36, "5"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [11, "3B"],
                [23, "C"],
                [18, "1B"],
                [7, "C"],
            ],
            "bullpen": [47, 57, 24, 44, 46, 76, 22, 56, 32, 37],
        },
        "home": {
            "team": "Kansas City Royals",
            "starter": 39,
            "roster": {
                # Lineup
                15: "Whit Merrifield",
                7: "Rosell Herrera",
                8: "Mike Moustakas",
                13: "Salvador Perez",
                38: "Jorge Bonifacio",
                17: "Hunter Dozier",
                21: "Lucas Duda",
                2: "Alcides Escobar",
                27: "Adalberto Mondesi",
                # Starting pitcher
                39: "Jason Hammel",
                # Bench
                9: "Drew Butera",
                4: "Alex Gordon",
                45: "Abraham Almonte",
                # Bullpen
                41: "Danny Duffy",
                50: "Jason Adam",
                61: "Kevin McCarthy",
                43: "Wily Peralta",
                64: "Burch Smith",
                33: "Brian Flynn",
                54: "Tim Hill",
                49: "Heath Fillmyer",
                37: "Brandon Maurer",
                72: "Enny Romero",
                65: "Jakob Junis",
                56: "Brad Keller",
            },
            "lefties": [41, 33, 54, 72],
            "lineup": [
                [15, "8"],
                [7, "9"],
                [8, "5"],
                [13, "2"],
                [38, "7"],
                [17, "0"],
                [21, "3"],
                [2, "6"],
                [27, "4"],
            ],
            "bench": [
                [9, "C"],
                [4, "LF"],
                [45, "OF"],
            ],
            "bullpen": [41, 50, 61, 43, 64, 33, 54, 49, 37, 72, 65, 56],
        },
        "umpires": {
            "HP": "Ryan Blakney",
            "1B": "Sam Holbrook",
            "2B": "Jim Wolf",
            "3B": "D.J. Reyburn",
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
# Pitching: KCR #39 Jason Hammel
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b f")
t1.hit(4)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b b c")
t1.out("F8")

# 3. BOS #28 J.D. Martinez (X - X - X)
t1.new_ab()
t1.pitch_list("f s b b b")
t1.hit(1)
t1.advance(2, "25 1B")
t1.advance(3, "2 BB")
t1.advance(4, "12 1B")

# 4. BOS #25 Steve Pearce (X - X - 28)
t1.new_ab()
t1.pitch_list("c b f")
t1.hit(1)
t1.advance(2, "2 BB")
t1.advance(4, "12 1B")

# 5. BOS #2  Xander Bogaerts (X - 28 - 25)
t1.new_ab(is_risp=True)
t1.pitch_list("c b d c b b")
t1.reach("BB")
t1.advance(3, "12 1B")
t1.advance(4, "3 1B")

# 6. BOS #12 Brock Holt (28 - 25 - 2)
t1.new_ab(is_risp=True)
t1.pitch_list("c b c f")
t1.hit(1, rbis=2)
t1.advance(2, "3 1B")

# 7. BOS #36 Eduardo Núñez (2 - X - 12)
t1.new_ab(is_risp=True)
t1.out("(F)P4")

# 8. BOS #3  Sandy León (2 - X - 12)
t1.new_ab(is_risp=True)
t1.pitch_list("f")
t1.hit(1, rbis=1)

# 9. BOS #19 Jackie Bradley Jr. (X - 12 - 3)
t1.new_ab(is_risp=True)
t1.pitch_list("b d b c c")
t1.out("G3")


# Bot 1st
# Pitching: BOS #41 Chris Sale
b1 = game.new_inning()

# 1. KCR #15 Whit Merrifield (X - X - X)
b1.new_ab()
b1.pitch_list("b b f f b")
b1.out("P4")

# 2. KCR #7  Rosell Herrera (X - X - X)
b1.new_ab()
b1.pitch_list("c b f b c")
b1.out("!K")

# 3. KCR #8  Mike Moustakas (X - X - X)
b1.new_ab()
b1.pitch_list("f f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: KCR #39 Jason Hammel
t2 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("F9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t2.new_ab()
t2.pitch_list("c b b")
t2.hit(1)
t2.advance(4, "28 HR")

# 3. BOS #28 J.D. Martinez (X - X - 16)
t2.new_ab()
t2.hit(4, rbis=2)

# 4. BOS #25 Steve Pearce (X - X - X)
t2.new_ab()
t2.hit(2)
t2.advance(4, "2 HR")

# 5. BOS #2  Xander Bogaerts (X - 25 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("c f f")
t2.hit(4, rbis=2)

# 6. BOS #12 Brock Holt (X - X - X)
t2.new_ab()
t2.pitch_list("c c")
t2.out("G4-3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("b c c b b")
t2.out("L6")


# Bot 2nd
# Pitching: BOS #41 Chris Sale
b2 = game.new_inning()

# 4. KCR #13 Salvador Perez (X - X - X)
b2.new_ab()
b2.pitch_list("c c f f b s")
b2.out("K")

# 5. KCR #38 Jorge Bonifacio (X - X - X)
b2.new_ab()
b2.hit(2)
b2.error(8)
b2.advance(3, "E8")
b2.advance(4, "2 1B")

# 6. KCR #17 Hunter Dozier (38 - X - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b c b b b")
b2.reach("BB")
b2.advance(2, "2 1B")

# 7. KCR #21 Lucas Duda (38 - X - 17)
b2.new_ab(is_risp=True)
b2.pitch_list("c b c b s")
b2.out("K")

# 8. KCR #2  Alcides Escobar (38 - X - 17)
b2.new_ab(is_risp=True)
b2.pitch_list("b b c f b")
b2.hit(1, rbis=1)

# 9. KCR #27 Adalberto Mondesi (X - 17 - 2)
b2.new_ab(is_risp=True)
b2.pitch_list("f f f b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: KCR #64 Burch Smith
t3 = game.new_inning()

# Pitching change (KCR): #64 Burch Smith replaces #39 Jason Hammel
t3.pitching_substitution(64)

# 8. BOS #3  Sandy León (X - X - X)
t3.new_ab()
t3.pitch_list("b c b f f b")
t3.out("G4-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("c s f b s")
t3.out("K2-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("c c b")
t3.out("F9")


# Bot 3rd
# Pitching: BOS #41 Chris Sale
b3 = game.new_inning()

# 1. KCR #15 Whit Merrifield (X - X - X)
b3.new_ab()
b3.pitch_list("c b f b s")
b3.out("K")

# 2. KCR #7  Rosell Herrera (X - X - X)
b3.new_ab()
b3.pitch_list("b s b s c")
b3.out("!K")

# 3. KCR #8  Mike Moustakas (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.out("(F)P5")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: KCR #64 Burch Smith
t4 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(1)

# 3. BOS #28 J.D. Martinez (X - X - 16)
t4.new_ab()
t4.pitch_list("s 1 c")
t4.out("L9")

# 4. BOS #25 Steve Pearce (X - X - 16)
t4.new_ab()
t4.pitch_list("b b c f f")
t4.out("P6")

# 5. BOS #2  Xander Bogaerts (X - X - 16)
t4.new_ab()
t4.pitch_list("c")
t4.out("G6-3")


# Bot 4th
# Pitching: BOS #41 Chris Sale
b4 = game.new_inning()

# 4. KCR #13 Salvador Perez (X - X - X)
b4.new_ab()
b4.pitch_list("s s b c")
b4.out("!K")

# 5. KCR #38 Jorge Bonifacio (X - X - X)
b4.new_ab()
b4.hit(1)

# 6. KCR #17 Hunter Dozier (X - X - 38)
b4.new_ab()
b4.pitch_list("b c s s")
b4.out("K")

# 7. KCR #21 Lucas Duda (X - X - 38)
b4.new_ab()
b4.pitch_list("c d f f s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: KCR #64 Burch Smith
t5 = game.new_inning()

# 6. BOS #12 Brock Holt (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.hit(1)
t5.thrown_out(2, "36 DP4-6-3", 1, 64)

# 7. BOS #36 Eduardo Núñez (X - X - 12)
t5.new_ab()
t5.pitch_list("s f b f f")
t5.out("DP4-6-3")

# 8. BOS #3  Sandy León (X - X - X)
t5.new_ab()
t5.pitch_list("b b")
t5.out("L9")


# Bot 5th
# Pitching: BOS #41 Chris Sale
b5 = game.new_inning()

# 8. KCR #2  Alcides Escobar (X - X - X)
b5.new_ab()
b5.pitch_list("b c b s")
b5.out("G4-3")

# 9. KCR #27 Adalberto Mondesi (X - X - X)
b5.new_ab()
b5.out("F9")

# 1. KCR #15 Whit Merrifield (X - X - X)
b5.new_ab()
b5.hit(2)

# 2. KCR #7  Rosell Herrera (X - 15 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c b b")
b5.out("G5-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: KCR #64 Burch Smith
t6 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t6.new_ab()
t6.pitch_list("c b s s")
t6.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("L8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t6.new_ab()
t6.pitch_list("b c c c")
t6.out("!K")


# Bot 6th
# Pitching: BOS #41 Chris Sale
b6 = game.new_inning()

# 3. KCR #8  Mike Moustakas (X - X - X)
b6.new_ab()
b6.pitch_list("c c")
b6.out("(F)P1")

# 4. KCR #13 Salvador Perez (X - X - X)
b6.new_ab()
b6.pitch_list("f b s")
b6.hit(1)

# 5. KCR #38 Jorge Bonifacio (X - X - 13)
b6.new_ab()
b6.pitch_list("b c c b c")
b6.out("!K")

# 6. KCR #17 Hunter Dozier (X - X - 13)
b6.new_ab()
b6.pitch_list("s s b b f d c")
b6.out("!K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: KCR #33 Brian Flynn
t7 = game.new_inning()

# Pitching change (KCR): #33 Brian Flynn replaces #64 Burch Smith
t7.pitching_substitution(33)

# 3. BOS #28 J.D. Martinez (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("F8")

# 4. BOS #25 Steve Pearce (X - X - X)
t7.new_ab()
t7.pitch_list("b b")
t7.out("G5-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t7.new_ab()
t7.pitch_list("c b s f b f")
t7.out("G5-3")


# Bot 7th
# Pitching: BOS #47 Tyler Thornburg
b7 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #41 Chris Sale
b7.pitching_substitution(47)

# 7. KCR #21 Lucas Duda (X - X - X)
b7.new_ab()
b7.pitch_list("b b c s f")
b7.hit(3)
b7.advance(4, "27 L4-3")

# 8. KCR #2  Alcides Escobar (21 - X - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b f f f")
b7.out("F8")

# 9. KCR #27 Adalberto Mondesi (21 - X - X)
b7.new_ab(is_risp=True)
b7.pitch_list("s")
b7.out("L4-3", rbis=1)

# 1. KCR #15 Whit Merrifield (X - X - X)
b7.new_ab()
b7.pitch_list("c b b f")
b7.out("L8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: KCR #33 Brian Flynn
t8 = game.new_inning()

# Defensive change (KCR): #9 Drew Butera replaces #13 Salvador Perez (C), playing C, batting 4th
t8.defensive_substitution(4, 9, "2")

# 6. BOS #12 Brock Holt (X - X - X)
t8.new_ab()
t8.pitch_list("f b c f")
t8.out("G4-3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t8.new_ab()
t8.pitch_list("b b")
t8.hit(2)
t8.advance(3, "3 F8")
t8.advance(4, "19 2B")

# 8. BOS #3  Sandy León (X - 36 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("c d f")
t8.out("F8")

# 9. BOS #19 Jackie Bradley Jr. (36 - X - X)
t8.new_ab(is_risp=True)
t8.pitch_list("d c s d")
t8.hit(2, rbis=1)

# 1. BOS #50 Mookie Betts (X - 19 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("b c")
t8.out("G6-3")


# Bot 8th
# Pitching: BOS #44 Brandon Workman
b8 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #47 Tyler Thornburg
b8.pitching_substitution(44)

# Defensive change (BOS): #23 Blake Swihart replaces #16 Andrew Benintendi (LF), playing LF, batting 2nd
b8.defensive_substitution(2, 23, "7")

# 2. KCR #7  Rosell Herrera (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.hit(1)
b8.advance(4, "8 HR")

# 3. KCR #8  Mike Moustakas (X - X - 7)
b8.new_ab()
b8.pitch_list("d c b b")
b8.hit(4, rbis=2)

# 4. KCR #9  Drew Butera (X - X - X)
b8.new_ab()
b8.pitch_list("c c b")
b8.out("G6-3")

# 5. KCR #38 Jorge Bonifacio (X - X - X)
b8.new_ab()
b8.pitch_list("b b c c")
b8.out("(F)P2")

# 6. KCR #17 Hunter Dozier (X - X - X)
b8.new_ab()
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: KCR #33 Brian Flynn
t9 = game.new_inning()

# 2. BOS #23 Blake Swihart (X - X - X)
t9.new_ab()
t9.pitch_list("b b")
t9.hit(1)
t9.advance(4, "25 2B")

# 3. BOS #28 J.D. Martinez (X - X - 23)
t9.new_ab()
t9.pitch_list("b f b f b f f f c")
t9.out("!K")

# 4. BOS #25 Steve Pearce (X - X - 23)
t9.new_ab()
t9.hit(2, rbis=1)
t9.advance(3, "36 WP")

# Pitching change (KCR): #37 Brandon Maurer replaces #33 Brian Flynn
t9.pitching_substitution(37)

# 5. BOS #2  Xander Bogaerts (X - 25 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("b d c c b f f d")
t9.reach("BB")
t9.advance(2, "36 WP")

# 6. BOS #12 Brock Holt (X - 25 - 2)
t9.new_ab(is_risp=True)
t9.out("L8")

# 7. BOS #36 Eduardo Núñez (X - 25 - 2)
t9.new_ab(is_risp=True)
t9.pitch_list("b c f f b")
t9.wp()
t9.out("(F)P1")


# Bot 9th
# Pitching: BOS #76 Hector Velázquez
b9 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #44 Brandon Workman
b9.pitching_substitution(76)

# 7. KCR #21 Lucas Duda (X - X - X)
b9.new_ab()
b9.pitch_list("c b b b")
b9.out("G4-3")

# 8. KCR #2  Alcides Escobar (X - X - X)
b9.new_ab()
b9.pitch_list("b c f f f")
b9.out("G5-3")

# 9. KCR #27 Adalberto Mondesi (X - X - X)
b9.new_ab()
b9.pitch_list("b b b c")
b9.hit(1)
b9.advance(2, "15 DI")
b9.advance(4, "15 1B")

# 1. KCR #15 Whit Merrifield (X - X - 27)
b9.new_ab(is_risp=True)
b9.pitch_list("b b f b")
b9.hit(1, rbis=1)

# 2. KCR #7  Rosell Herrera (X - X - 15)
b9.new_ab()
b9.pitch_list("f")
b9.out("G4-3")

# Winning team: BOS
# WP: BOS #41 Chris Sale
game.winning_pitcher(41, is_away_team=True)

# Loser team: KCR
# LP: KCR #39 Jason Hammel
game.losing_pitcher(39)

# print(game)
game.generate_scorecard()
