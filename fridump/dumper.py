import os
import logging

# Reading bytes from session and saving it to a file

def dump_to_file(session,base,size,error,directory):
        try:
                filename = str(hex(base))+'_dump.data'
                logging.debug("file name:"+str(filename))
                dump =  session.read_bytes(base, size)
                logging.debug("dump size:"+str(dump.size))
                f = open(os.path.join(directory,filename), 'wb')
                f.write(dump)
                f.close()
                return error
        except:
               print "Oops, memory access violation!"

               return error

#Read bytes that are bigger than the max_size value, split them into chunks and save them to a file

def splitter(session,base,size,max_size,error,directory):
        times = size/max_size
        logging.debug("value of max_size:"+str(max_size))
        logging.debug("value of times:"+str(times))

        diff = size % max_size
        logging.debug("value of diff:"+str(diff))

        if diff is 0:
            logging.debug("Number of chunks:"+str(times+1))
        else:
            logging.debug("Number of chunks:"+str(times))
        global cur_base
        cur_base = base
        logging.debug("value of cur_base:"+str(hex(cur_base)))

        for time in range(times):
                logging.debug("Save bytes "+str(time)+": "+str(hex(cur_base))+" till "+str(hex(cur_base+max_size)) + " on " + str(directory))
                dump_to_file(session, cur_base, max_size, error, directory)
                cur_base = cur_base + max_size

        if diff is not 0:
            logging.debug("Save bytes: "+str(hex(cur_base))+" till "+str(hex(cur_base+diff)) + " on " + str(directory))
            dump_to_file(session, cur_base, diff, error, directory)

