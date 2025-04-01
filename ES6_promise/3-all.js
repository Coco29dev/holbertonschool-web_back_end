import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([Photo, User]) => {
      console.log(Photo.body, User.firstName, User.lastName);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
