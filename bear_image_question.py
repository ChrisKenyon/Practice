# image matching challenge
# background: visual slam
# given: 1. an array of images 2. a new image
# challenge: return the index of best matching image if any, and its matching score (0-10)

# design the Image class. assuming an image is represented by 10 features, each feature being a fixed length string


class Image(object):
    '''
        An Image class that represents a visual SLAM image taken
        Holds 10 unique features

    '''
    def __init__(self, features):
        '''
            features is a set() of fixed length strings
        '''
        self.features = features

    # assuming length of features is N, what's the complexity? -> O(N)
    def compare(self, image):
        '''
            Given image as an Image object,
            compare will compare the features of self and image
            and return an int score representing # of matches
        '''

        score = 0
        for feature in self.features:
            if feature in image.features:
                score+=1

        return score


    # assuming length of images is M, what's the complexity? -> O(M * N), space -> O(1)
    def best_image_match(images, new_image):
        '''
            Given an array of Image objects (images) and a new Image object (new_image),
            return the int index of the best matching Image in images
        '''
        best = new_image.compare(images[0])
        for i in range(1,len(images)):
            best = max(best, new_image.compare(images[i]))

        return best if best > 0 else -1


    # here is problem -> what if M is really really large ?

    # feature_cache
    { 'a':[0,1,2]
      'b':[2,3]  }

    #counts
    {
        0: 1
        1: 1
        2: 2
        3: 1
    }

    # comment...
    feature_cache = dict()

    def add_to_cache(image, idx):
        '''
            ....
        '''
        for feature in image.features:
            if feature not in feature_cache:
                feature_cache[feature] = [idx]
            else:
                feature_cache[feature].append(idx)


    from collections import Counter

    def best_image_match2(images, new_image)
        ''':
            Optimized solution to best_image_match
        '''
        counts = Counter()
        for feature in new_image.features:
            for idx in feature_cache[feature]:
                counts.add(idx)



        # Must maintain invariant that this image is added to images
        add_to_cache(new_image,len(images))


        return #max_key(counts)



    # assuming M images, X total features globally, evenly distributed
    # M*N^2/X


    # write a ROS node, which takes in twist topic /mobile_base/commands/velocity_raw, and outputs it as /mobile_base/commands/velocity


