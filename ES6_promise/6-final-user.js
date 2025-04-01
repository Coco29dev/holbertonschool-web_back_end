import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const user = signUpUser(firstName, lastName);
  const photo = uploadPhoto(fileName);
  const promises = [user, photo];
  return Promise.allSettled(promises)
    .then((resultats) => resultats.map((resultat) => {
      if (resultat.status === 'rejected') {
        return { status: resultat.status, value: resultat.reason };
      }
      return { status: resultat.status, value: resultat.reason };
    }));
}
