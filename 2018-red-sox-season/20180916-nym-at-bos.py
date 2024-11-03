import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYM @ BOS, 2018-09-16
# https://www.baseball-reference.com/boxes/BOS/BOS201809160.shtml
# https://www.mlb.com/gameday/mets-vs-red-sox/2018/09/16/531642/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-16 13:06-16:01",
        "at": "Fenway Park, Boston, MA",
        "att": "36,526",
        "temp": "84F, Sunny",
        "wind": "7mph, In From RF",
        "away": {
            "team": "New York Mets",
            "starter": 48,
            "roster": {
                # Lineup
                1: "Amed Rosario",
                68: "Jeff McNeil",
                4: "Wilmer Flores",
                30: "Michael Conforto",
                21: "Todd Frazier",
                19: "Jay Bruce",
                9: "Brandon Nimmo",
                26: "Kevin Plawecki",
                16: "Austin Jackson",
                # Starting pitcher
                48: "Jacob deGrom",
                # Bench
                3: "Tomás Nido",
                29: "Devin Mesoraco",
                22: "Dominic Smith",
                7: "José Reyes",
                72: "Jack Reinheimer",
                59: "Jose Lobaton",
                # Bullpen
                32: "Steven Matz",
                45: "Zack Wheeler",
                34: "Noah Syndergaard",
                73: "Daniel Zamora",
                49: "Tyler Bashlor",
                70: "Eric Hanhold",
                63: "Tim Peterson",
                51: "Paul Sewald",
                35: "Jacob Rhame",
                55: "Corey Oswalt",
                62: "Drew Smith",
                47: "Drew Gagnon",
                39: "Jerry Blevins",
                65: "Robert Gsellman",
                67: "Seth Lugo",
                38: "Anthony Swarzak",
                40: "Jason Vargas",
            },
            "lefties": [32, 73, 39, 40],
            "lineup": [
                [1, "6"],
                [68, "4"],
                [4, "3"],
                [30, "7"],
                [21, "5"],
                [19, "0"],
                [9, "9"],
                [26, "2"],
                [16, "8"],
            ],
            "bench": [
                [3, "C"],
                [29, "C"],
                [22, "1B"],
                [7, "SS"],
                [72, "SS"],
                [59, "C"],
            ],
            "bullpen": [32, 45, 34, 73, 49, 70, 63, 51, 35, 55, 62, 47, 39, 65, 67, 38, 40],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                12: "Brock Holt",
                16: "Andrew Benintendi",
                25: "Steve Pearce",
                18: "Mitch Moreland",
                5: "Ian Kinsler",
                19: "Jackie Bradley Jr.",
                11: "Rafael Devers",
                7: "Christian Vázquez",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                30: "Tzu-Wei Lin",
                36: "Eduardo Núñez",
                59: "Sam Travis",
                28: "J.D. Martinez",
                23: "Blake Swihart",
                2: "Xander Bogaerts",
                3: "Sandy León",
                0: "Brandon Phillips",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                67: "William Cuevas",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                63: "Robby Scott",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [41, 57, 31, 61, 66, 63, 24],
            "lineup": [
                [50, "9"],
                [12, "6"],
                [16, "7"],
                [25, "0"],
                [18, "3"],
                [5, "4"],
                [19, "8"],
                [11, "5"],
                [7, "2"],
            ],
            "bench": [
                [30, "OF"],
                [36, "SS"],
                [59, "1B"],
                [28, "DH"],
                [23, "C"],
                [2, "2B"],
                [3, "C"],
                [0, "2B"],
            ],
            "bullpen": [47, 57, 35, 44, 67, 22, 31, 61, 66, 37, 63, 24, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Bill Miller",
            "1B": "Angel Hernandez",
            "2B": "Todd Tichenor",
            "3B": "Chad Whitson",
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
# Pitching: BOS #41 Chris Sale
t1 = game.new_inning()

# 1. NYM #1  Amed Rosario (X - X - X)
t1.new_ab()
t1.out("F8")

# 2. NYM #68 Jeff McNeil (X - X - X)
t1.new_ab()
t1.pitch_list("c b b b")
t1.out("G3-1")

# 3. NYM #4  Wilmer Flores (X - X - X)
t1.new_ab()
t1.pitch_list("b s s")
t1.out("G5-3")


# Bot 1st
# Pitching: NYM #48 Jacob deGrom
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c s b f f b b c")
b1.out("!K")

# 2. BOS #12 Brock Holt (X - X - X)
b1.new_ab()
b1.pitch_list("t c s")
b1.out("K")

# 3. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b c b c f")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 Chris Sale
t2 = game.new_inning()

# 4. NYM #30 Michael Conforto (X - X - X)
t2.new_ab()
t2.pitch_list("s b c f f f b f")
t2.out("G6-3")

# 5. NYM #21 Todd Frazier (X - X - X)
t2.new_ab()
t2.pitch_list("b b c f s")
t2.out("K")

# 6. NYM #19 Jay Bruce (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.hit(1)
t2.thrown_out(2, "9 CS", 3, 41)

# 7. NYM #9  Brandon Nimmo (X - X - 19)
t2.new_ab()
t2.pitch_list("b b c c b")
t2.no_ab("CS")


# Bot 2nd
# Pitching: NYM #48 Jacob deGrom
b2 = game.new_inning()

# 4. BOS #25 Steve Pearce (X - X - X)
b2.new_ab()
b2.pitch_list("c c s")
b2.out("K")

# 5. BOS #18 Mitch Moreland (X - X - X)
b2.new_ab()
b2.pitch_list("f b f c")
b2.out("!K")

# 6. BOS #5  Ian Kinsler (X - X - X)
b2.new_ab()
b2.pitch_list("c c f b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 Chris Sale
t3 = game.new_inning()

# 7. NYM #9  Brandon Nimmo (X - X - X)
t3.new_ab()
t3.pitch_list("b b c s")
t3.out("(F)P2")

# 8. NYM #26 Kevin Plawecki (X - X - X)
t3.new_ab()
t3.pitch_list("c c b")
t3.out("F8")

# 9. NYM #16 Austin Jackson (X - X - X)
t3.new_ab()
t3.pitch_list("s")
t3.out("G3")


# Bot 3rd
# Pitching: NYM #48 Jacob deGrom
b3 = game.new_inning()

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("s s b b f s")
b3.out("K")

# 8. BOS #11 Rafael Devers (X - X - X)
b3.new_ab()
b3.pitch_list("s f")
b3.hit(1)
b3.advance(3, "7 1B")
b3.advance(4, "50 SF8")

# 9. BOS #7  Christian Vázquez (X - X - 11)
b3.new_ab()
b3.hit(1)
b3.advance(4, "12 HR")

# 1. BOS #50 Mookie Betts (11 - X - 7)
b3.new_ab(is_risp=True)
b3.pitch_list("s b")
b3.out("SF8", rbis=1)

# 2. BOS #12 Brock Holt (X - X - 7)
b3.new_ab()
b3.pitch_list("b")
b3.hit(4, rbis=2)

# 3. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.out("L6")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #76 Hector Velázquez
t4 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #41 Chris Sale
t4.pitching_substitution(76)

# 1. NYM #1  Amed Rosario (X - X - X)
t4.new_ab()
t4.pitch_list("c s")
t4.out("G6-3")

# 2. NYM #68 Jeff McNeil (X - X - X)
t4.new_ab()
t4.pitch_list("b c f")
t4.out("G6-3")

# 3. NYM #4  Wilmer Flores (X - X - X)
t4.new_ab()
t4.reach("HBP")
t4.advance(2, "30 1B")
t4.advance(3, "21 WP")

# 4. NYM #30 Michael Conforto (X - X - 4)
t4.new_ab()
t4.pitch_list("b b f f")
t4.hit(1)
t4.advance(2, "21 WP")

# 5. NYM #21 Todd Frazier (X - 4 - 30)
t4.new_ab(is_risp=True)
t4.pitch_list("b c b c f f")
t4.wp()
t4.out("(F)P5")


# Bot 4th
# Pitching: NYM #48 Jacob deGrom
b4 = game.new_inning()

# 4. BOS #25 Steve Pearce (X - X - X)
b4.new_ab()
b4.pitch_list("c s b b f b f b")
b4.reach("BB")

# 5. BOS #18 Mitch Moreland (X - X - 25)
b4.new_ab()
b4.pitch_list("f f b d c")
b4.out("!K")

# 6. BOS #5  Ian Kinsler (X - X - 25)
b4.new_ab()
b4.pitch_list("f c s")
b4.out("K")

# 7. BOS #19 Jackie Bradley Jr. (X - X - 25)
b4.new_ab()
b4.pitch_list("b b c")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #31 Drew Pomeranz
t5 = game.new_inning()

# Pitching change (BOS): #31 Drew Pomeranz replaces #76 Hector Velázquez
t5.pitching_substitution(31)

# 6. NYM #19 Jay Bruce (X - X - X)
t5.new_ab()
t5.pitch_list("c b f b f b")
t5.out("L9")

# 7. NYM #9  Brandon Nimmo (X - X - X)
t5.new_ab()
t5.pitch_list("s s b b b f")
t5.out("L9")

# 8. NYM #26 Kevin Plawecki (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G6-3")


# Bot 5th
# Pitching: NYM #48 Jacob deGrom
b5 = game.new_inning()

# 8. BOS #11 Rafael Devers (X - X - X)
b5.new_ab()
b5.pitch_list("f b b")
b5.out("F7")

# 9. BOS #7  Christian Vázquez (X - X - X)
b5.new_ab()
b5.pitch_list("b c s f b c")
b5.out("!K")

# 1. BOS #50 Mookie Betts (X - X - X)
b5.new_ab()
b5.pitch_list("b c c s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #31 Drew Pomeranz
t6 = game.new_inning()

# 9. NYM #16 Austin Jackson (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.hit(1)
t6.advance(3, "1 2B")
t6.advance(4, "4 SF9")

# 1. NYM #1  Amed Rosario (X - X - 16)
t6.new_ab()
t6.pitch_list("d s f f 1 b d f")
t6.hit(2)
t6.advance(3, "30 PB")
t6.advance(4, "30 2B")

# 2. NYM #68 Jeff McNeil (16 - 1 - X)
t6.new_ab(is_risp=True)
t6.out("L9")

# 3. NYM #4  Wilmer Flores (16 - 1 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b s d")
t6.out("SF9", rbis=1)

# Defensive change (BOS): #30 Tzu-Wei Lin replaces #50 Mookie Betts (RF), playing CF, batting 1st
t6.defensive_substitution(1, 30, "8")

# Defensive switch (BOS): #19 Jackie Bradley Jr. moves to RF
t6.defensive_switch(19, "9")

# 4. NYM #30 Michael Conforto (X - 1 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b c")
t6.pb()
t6.hit(2, rbis=1)

# Pitching change (BOS): #37 Heath Hembree replaces #31 Drew Pomeranz
t6.pitching_substitution(37)

# 5. NYM #21 Todd Frazier (X - 30 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b f b f f f b")
t6.out("G5-3")


# Bot 6th
# Pitching: NYM #48 Jacob deGrom
b6 = game.new_inning()

# 2. BOS #12 Brock Holt (X - X - X)
b6.new_ab()
b6.pitch_list("c b b c c")
b6.out("!K")

# 3. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("F7")

# 4. BOS #25 Steve Pearce (X - X - X)
b6.new_ab()
b6.hit(2)

# 5. BOS #18 Mitch Moreland (X - 25 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("c b")
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #37 Heath Hembree
t7 = game.new_inning()

# 6. NYM #19 Jay Bruce (X - X - X)
t7.new_ab()
t7.pitch_list("f b s b f b b")
t7.reach("BB")
t7.advance(2, "9 HBP")
t7.advance(4, "1 1B")

# 7. NYM #9  Brandon Nimmo (X - X - 19)
t7.new_ab()
t7.pitch_list("b c 1")
t7.reach("HBP")
t7.error(8)
t7.advance(2, "1 1B")
t7.advance(3, "1 E8")

# Pitching change (BOS): #56 Joe Kelly replaces #37 Heath Hembree
t7.pitching_substitution(56)

# 8. NYM #26 Kevin Plawecki (X - 19 - 9)
t7.new_ab(is_risp=True)
t7.pitch_list("l s f s")
t7.out("K")

# 9. NYM #16 Austin Jackson (X - 19 - 9)
t7.new_ab(is_risp=True)
t7.pitch_list("c")
t7.out("F9")

# 1. NYM #1  Amed Rosario (X - 19 - 9)
t7.new_ab(is_risp=True)
t7.hit(1, rbis=1)

# 2. NYM #68 Jeff McNeil (9 - X - 1)
t7.new_ab(is_risp=True)
t7.pitch_list("b b s 1 1 b s")
t7.out("G6-3")


# Bot 7th
# Pitching: NYM #48 Jacob deGrom
b7 = game.new_inning()

# 6. BOS #5  Ian Kinsler (X - X - X)
b7.new_ab()
b7.pitch_list("c b f f b")
b7.out("F9")

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("f b s")
b7.hit(1)
b7.advance(2, "11 SB")

# 8. BOS #11 Rafael Devers (X - X - 19)
b7.new_ab(is_risp=True)
b7.pitch_list("1 f s b c")
b7.out("!K")

# 9. BOS #7  Christian Vázquez (X - 19 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b b")
b7.out("F7")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #44 Brandon Workman
t8 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #56 Joe Kelly
t8.pitching_substitution(44)

# 3. NYM #4  Wilmer Flores (X - X - X)
t8.new_ab()
t8.pitch_list("b c b f f b f d")
t8.reach("BB")
# Offensive change (NYM): Pinch-runner #72 Jack Reinheimer replaces #4 Wilmer Flores
t8.offensive_substitution(3, 72, "PR")
t8.atbase("PR")
t8.thrown_out(2, "30 POCS", 1, 44)

# 4. NYM #30 Michael Conforto (X - X - 4)
t8.new_ab()
t8.pitch_list("1 b 1 b s c s")
t8.out("K")

# 5. NYM #21 Todd Frazier (X - X - X)
t8.new_ab()
t8.pitch_list("b c b c b s")
t8.out("K")


# Bot 8th
# Pitching: NYM #67 Seth Lugo
b8 = game.new_inning()

# Pitching change (NYM): #67 Seth Lugo replaces #48 Jacob deGrom
b8.pitching_substitution(67)

# Defensive change (NYM): #22 Dominic Smith replaces #72 Jack Reinheimer (PR), playing 1B, batting 3rd
b8.defensive_substitution(3, 22, "3")

# 1. BOS #30 Tzu-Wei Lin (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.hit(2)
b8.advance(3, "12 F8")
b8.advance(4, "16 SF8")

# 2. BOS #12 Brock Holt (X - 30 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b b")
b8.out("F8")

# 3. BOS #16 Andrew Benintendi (30 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("t")
b8.out("SF8", rbis=1)

# 4. BOS #25 Steve Pearce (X - X - X)
b8.new_ab()
b8.pitch_list("s f f f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #35 Steven Wright
t9 = game.new_inning()

# Pitching change (BOS): #35 Steven Wright replaces #44 Brandon Workman
t9.pitching_substitution(35)

# 6. NYM #19 Jay Bruce (X - X - X)
t9.new_ab()
t9.out("G4-3")

# 7. NYM #9  Brandon Nimmo (X - X - X)
t9.new_ab()
t9.pitch_list("b c b b b")
t9.reach("BB")

# 8. NYM #26 Kevin Plawecki (X - X - 9)
t9.new_ab()
t9.pitch_list("b c")
t9.out("P4")

# 9. NYM #16 Austin Jackson (X - X - 9)
t9.new_ab()
t9.pitch_list("b b 1 c c c")
t9.out("!K")

# Winning team: BOS
# WP: BOS #44 Brandon Workman
game.winning_pitcher(44)
# SV: BOS #35 Steven Wright
game.save_pitcher(35)

# Loser team: NYM
# LP: NYM #67 Seth Lugo
game.losing_pitcher(67, is_away_team=True)

# print(game)
game.generate_scorecard()
